double = lambda x: x + x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
three = lambda f: lambda x: f(f(f(x)))
four = lambda f: lambda x: f(f(f(f(x))))
eight = lambda f: lambda x: f(f(f(f(f(f(f(f(x))))))))
test = """\
p(two)(one)(double)(1) == 4 and \
p(one)(two)(double)(1) == 2 and \
p(two)(two)(double)(1) == 16 and \
p(two)(three)(double)(1) == 256 \
"""
