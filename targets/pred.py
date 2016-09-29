# p(m) = m - 1 if m > 0 else 0 (for church numbers)

one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
succ = lambda x: x + 1
test = "p(one)(succ)(0) == 0 and p(two)(succ)(0) == 1"

# ???
