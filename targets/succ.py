# p(m) = m + 1 in church numerals

one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
succ = lambda x: x + 1
test = "p(one)(succ)(0) == 2 and p(two)(succ)(0) == 3"

# (0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0)
