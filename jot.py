# Jot Interpreter
from functools import reduce

ski_S = lambda x: lambda y: lambda z: (x(z))(y(z))
ski_I = lambda x: x
ski_K = lambda x: lambda y: x

def jot_to_py(code):
    def process_char(accum, char):
        if char == '1':
            return lambda f: lambda a: accum(f(a))
        elif char == '0':
            return accum(ski_S)(ski_K)

    return reduce(process_char, code, ski_I)
