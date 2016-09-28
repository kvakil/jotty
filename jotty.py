# Jotty Autoprogrammer
from jot import jot_to_py

def test_program(code, tests):
    """Returns True if the given code satisfies all the tests."""
    p = jot_to_py(code)
    for test in tests:
        if not eval(test):
            return False
    else:
        return True

def program_to_code(program, length=0):
    """Converts a number to a string which can be executed by jot_to_py.
    >>> program_to_code(6)
    110
    >>> program_to_code(5, 7)
    0000101
    """
    return bin(program)[2:].zfill(length)

def test_bitstrings(length, tests):
    """Tests all bitstrings of a given length to see if any of them, when
    interpreted as jot code, satisfy all the tests.

    Prints out the code if it finds it.""" 
    max_program = 2 ** length
    for program in range(max_program):
        code = program_to_code(program, length)
        try:
            if test_program(code, tests):
                print('FOUND:', code)
                return True
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            pass
    return False

# import and compile tests
from target import *
tests = [compile(test, 'target', 'eval') for test in tests]

length = 0
while True:
    print(length)
    if test_bitstrings(length, tests):
        break
    length += 1
