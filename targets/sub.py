one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
succ = lambda x: x + 1
test = "p(two)(one)(succ)(0) == 1 and p(one)(two)(succ)(0) == 0"
