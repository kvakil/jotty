# Jotty Autoprogrammer
from jot import jot_to_py
from itertools import product

def test_program(code, test):
    """Returns True if the given code satisfies the test."""
    p = jot_to_py(code)
    return eval(test)

def test_bitstrings(length, test):
    """Tests all bitstrings of a given length to see if any of them, when
    interpreted as jot code, satisfy the test.

    Prints out the code if it finds it."""
    for program in product([0, 1], repeat=length):
        try:
            if test_program(program, test):
                print('FOUND:', program)
                return True
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            pass
    return False

# import and compile tests
from target import *
test = compile(test, 'target', 'eval')

length = 0
while True:
    print(length)
    if test_bitstrings(length, test):
        break
    length += 1
