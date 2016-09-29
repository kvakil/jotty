# p(0) = 1 and p(1) = 0

zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
succ = lambda x: x + 1
test = 'p(zero)(succ)(0) == 1 and p(one)(succ)(0) == 0'

# (0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0)
