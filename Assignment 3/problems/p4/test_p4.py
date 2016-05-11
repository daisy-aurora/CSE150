"""For each input in in/input*.txt, you can invoke this file as:

    python test_p4.py submitted_file.py <inputfile >out.txt
    
"""

import os
import sys
import operator

from assignment3 import *

def run_code_from(python_file, input_text):
    # Load the class from the specified .py file
    sys.path.append(os.path.abspath(os.path.dirname(python_file)))
    module = __import__(os.path.splitext(os.path.basename(python_file))[0])
    test_method = getattr(module, 'ac3')
    exec (input_text, globals(), locals())
    arcs = locals()['test_arcs'] if 'test_arcs' in locals() else None
    return str(test_method(locals()['csp'], arcs))


if __name__ == '__main__':
    print(run_code_from(sys.argv[1], sys.stdin.read().strip()))