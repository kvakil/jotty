# p(n) = 2 * n for church numbers

two = lambda f: lambda x: f(f(x))
three = lambda f: lambda x: f(f(f(x)))
succ = lambda x: x + 1
test = "p(two)(succ)(0) == 4 and p(three)(succ)(0) == 6"

# (0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1)
