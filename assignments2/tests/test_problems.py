# -*- coding: utf-8 -*-

__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from unittest import main, TestCase
from glob import glob
import sys
import os.path as op

DEBUG = False

# Set the name here
if DEBUG:
    SOLUTIONS_DIR = '../OFFICIAL_SOLUTIONS/'
else:
    SOLUTIONS_DIR = '../solutions/'

PYTHON_NAMES = dict([
    ('p1', 'p1_minimax_player.py'),
    ('p2', 'p2_alphabeta_player.py'),
    ('p3', 'p3_evaluation_player.py'),
    ('p4', 'p4_custom_player.py')
])

# Add the src directory
sys.path.append('../src')

class TestProblems(TestCase):
    def setUp(self):
        pass


def test_generator(test_module, player_file, infile, outfile):
    def test(self):
        with open(infile, 'r') as f:
            input = f.read()

        with open(outfile, 'r') as f:
            output = f.read()

        actual = test_module.run_code_from(player_file, input).strip()
        self.assertEqual(output, actual)

    return test


for problem_dir in glob('../problems/p*'):
    problem = op.basename(problem_dir)
    for infile in glob(op.join(problem_dir, 'in', 'input*.txt')):
        input_name = op.splitext(op.basename(infile))[0]
        outfile = op.join(problem_dir, 'out', 'output' + input_name.split('input')[-1] + '.txt')
        name = '%s_%s' % (problem, input_name)

        player_file = op.join(op.abspath(SOLUTIONS_DIR), PYTHON_NAMES[problem])

        # Load the test file
        sys.path.append(op.abspath(problem_dir))
        test_module = __import__('test_single_p')
        setattr(TestProblems, 'test_%s' % name, test_generator(test_module, player_file, infile, outfile))
        sys.path.remove(op.abspath(problem_dir))


if __name__ == '__main__':
    main()