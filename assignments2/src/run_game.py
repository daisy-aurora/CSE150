# -*- coding: utf-8 -*-
"""Contains routines for running the game."""
import random
import os

from types import MethodType
from multiprocessing import Process, Queue

__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

DEBUG = False

try:
    from queue import Empty
except ImportError:
    from Queue import Empty

from assignment2 import Player, State, Action


class Game(object):
    def __init__(self, M, N, player_classes, timeout=None):
        self.players = Player.create_players(player_classes)
        self.state = State.initial(M, N, self.players[0])
        self.timeout = timeout

    def play(self):
        while not self.state.is_terminal():
            self.before_move()
            next_move = self.request_move()
            print str(next_move)
            self.state = self.state.result(next_move)
            self.after_move()

        return self.state.winner_row

    def request_move(self):
        # state = copy.deepcopy(self.state)
        state = self.state
        player = self.state.player

        if self.timeout is None:
            # No timeout, just use a single process
            action = self.state.player.move(state)
        else:
            # For passing the messages back and forth
            self.result_q = Queue(1)
            self.signal_q = Queue(1)

            # Dynamically augment the player instance
            def is_time_up(self):
                if not self._timeup:
                    try:
                        self._signal_q.get_nowait()
                        self._timeup = True
                    except Empty:
                        return False
                return True

            def _do_move(self, state, result_q, signal_q):
                sys.stdin = os.fdopen(self.fileno)
                self._signal_q = signal_q
                action = self.move(state)
                members = [(attr, v) for attr, v in vars(self).items()
                           if (not callable(getattr(self, attr)) and not attr.startswith("__")
                           and not attr in ['_signal_q', '_timeup', 'fileno', 'next', 'row'])]
                result_q.put_nowait((action, members))

            player.is_time_up = MethodType(is_time_up, player)
            player._do_move = MethodType(_do_move, player)
            player.fileno = sys.stdin.fileno()
            player._timeup = False

            # Boot a process for the player move
            move_process = Process(target=player._do_move, args=(state, self.result_q, self.signal_q))
            move_process.start()

            action = None
            player_vars = None
            is_time_out = False
            try:
                action, player_vars = self.result_q.get(True, self.timeout)

            except Empty:
                # Send the "time is up" warning
                self.signal_q.put_nowait(0)

                # Wait one second and get the move
                try:
                    action, player_vars = self.result_q.get(True, 1)
                except Empty:
                    is_time_out = True

            # Clear queues
            try:
                self.signal_q.get_nowait()
            except Empty:
                pass

            try:
                self.result_q.get_nowait()
            except Empty:
                pass

            if move_process.is_alive():
                move_process.terminate()
                move_process.join(1)

            if is_time_out:
                print("Time is up and no valid move was returned, playing a random move.")
                # If a move wasn't placed on the result pipe in time, play a random move
                actions = state.actions()
                if not actions:
                    return None

                return random.choice(actions)


            if player_vars is not None:
                for key, value in player_vars:
                    setattr(player, key, value)

        return action


class ConsoleGame(Game):
    def before_move(self):
        print repr(self.state)
        print('')

    def after_move(self):
        pass

    def play(self):
        winner_row = super(ConsoleGame, self).play()

        print repr(self.state)

        if winner_row == -1:
            print "Draw!"
            return None
        else:
            winner = next((player for player in self.players if player.row == winner_row))
            print("%s won!" % str(winner))
            return winner


if __name__ == '__main__':
    import sys
    import glob
    import os.path as op
    import inspect

    if len(sys.argv) < 4:
        print("%s: M N timeout player1_class player2_class" % sys.argv[0])

    sys.argv.pop(0)
    M = int(sys.argv.pop(0))
    N = int(sys.argv.pop(0))
    timeout = int(sys.argv.pop(0))
    if timeout == -1:
        timeout = None

    player_names = sys.argv

    # Load all player classes from *_player.py files
    # in the current directory and solutions directory
    if not DEBUG:
        player_files = glob.glob('*_player.py') + glob.glob(
            '../solutions/*_player.py')
    else:
        player_files = glob.glob('*_player.py') + glob.glob(
            '../OFFICIAL_SOLUTIONS/*_player.py')
    for player_file in player_files:
        sys.path.append(op.abspath(op.dirname(player_file)))

    modules = [__import__(op.splitext(op.basename(f))[0]) for f in player_files]
    names = dict([(name, module) for module in modules for name in dir(module) if
                  inspect.isclass(getattr(module, name)) and issubclass(getattr(module, name), Player) and \
                  getattr(module, name) != Player])
    player_classes = [getattr(names[name], name) for name in player_names]

    game = ConsoleGame(M, N, player_classes, timeout)
    game.play()