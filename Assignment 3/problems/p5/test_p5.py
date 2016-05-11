"""For each input in in/input*.txt, you can invoke this file as:

    python test_p5.py submitted_file.py <inputfile >out.txt
    
"""

import os
import sys
import operator

from assignment3 import *

def run_code_from(python_file, input_text):
    # Load the class from the specified .py file
    sys.path.append(os.path.abspath(os.path.dirname(python_file)))
    module = __import__(os.path.splitext(os.path.basename(python_file))[0])

    exec (input_text, globals(), locals())
    if 'variable' in locals():
        test_method2 = getattr(module, 'order_domain_values')
        values = test_method2(locals()['csp'], locals()['variable'])
        return str(values)
    else:
        test_method1 = getattr(module, 'select_unassigned_variable')
        var = test_method1(locals()['csp'])
        return str(var.name)


if __name__ == '__main__':
    print(run_code_from(sys.argv[1], sys.stdin.read().strip()))