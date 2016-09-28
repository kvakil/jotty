# Jot Interpreter
from functools import reduce

ski_S = lambda x: lambda y: lambda z: (x(z))(y(z))
ski_I = lambda x: x
ski_K = lambda x: lambda y: x

def jot_to_py(code):
    """Tests:
    >>> jot_to_py('')('Identity!')
    'Identity!'
    >>> # K combinator
    >>> jot_to_py('11100')(42)(17)
    42
    >>> # S combinator
    >>> add = lambda x: lambda y: x + y
    >>> double = lambda x: add(x)(x)
    >>> jot_to_py('11111000')(add)(double)(4)
    12
    >>> # I combinator with S and K
    >>> jot_to_py('11111110001110011100')('Identity!')
    'Identity!'
    >>> # infinite loop
    >>> jot_to_py('11111111000111111111000001111111110000011111110001111111110\
000011111111100000')
    Traceback (most recent call last):
        ...
    RecursionError: maximum recursion depth exceeded
    """
    def process_char(accum, char):
        if char == '1':
            return lambda f: lambda a: accum(f(a))
        elif char == '0':
            return accum(ski_S)(ski_K)

    return reduce(process_char, code, ski_I)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
