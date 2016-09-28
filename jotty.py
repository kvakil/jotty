# Jotty Autoprogrammer
from jot import jot_to_py

def test_program(code, tests):
    p = jot_to_py(code)
    for test in tests:
        if eval(test[0]) != test[1]:
            return False
    else:
        return True

MAX_PROG = 2 ** 32

tupler = lambda x: lambda y: (x, y)
tests = [(compile('p(1)', '<string>', 'eval'), 1)]
for program in range(MAX_PROG):
    code = bin(program)[2:]
    try:
        if test_program(code, tests):
            print(code)
            break
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        pass
