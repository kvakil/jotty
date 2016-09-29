# p(x)(y)(z) = x(z)(y(z)) (S combinator)
square = lambda x: x * x
add = lambda x: lambda y: x + y
test = 'p(add)(square)(3) == 12'

# (0, 0, 0)
