# p(m)(n) = m^n for church numbers

one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
succ = lambda x: x + 1
test = "p(two)(two)(succ)(0) == 4 and p(one)(two)(succ)(0) == 1"

# (0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0)
