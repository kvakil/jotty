# Jotty

An Jot interpreter and programmer written in Python.

## About Jot

Jot is a programming language where any sequence of 0s and 1s is a valid program. [Read more about Jot here.](//esolangs.org/wiki/Jot)

## About Jotty

As anticipated, writing programs in Jot is painful. Jotty works by searching through all possible programs for another program which is [extensionally equal](//en.wikipedia.org/wiki/Deductive_lambda_calculus#Intensional_versus_extensional_equality) to the desired program. For example, say we want to find a program which creates the K-combinator. The K-combinator takes two arguments, and returns the first one. Here is some Python code to illustrate:

    ski_K = lambda x: lambda y: x
    ski("fish")(42) == "fish"

We begin by creating the file `target/k_combinator.py`, which tells Jotty what we need:

    # target/k_combinator.py: return the first argument, discard the second
    test = 'p(1)(2) == 1'

Now we can use jotty to try to bruteforce a solution:

    $ ./jotty target/k_combinator.py
    (0, 0)

Jotty has found the Jot program `00`. We can verify that this gives the correct result. First we convert from Jot to SKI:

    [00] = [0]SK = []SKSK = ISKSK

Now using the rules of [SKI-combinator calculus](//en.wikipedia.org/wiki/SKI_combinator_calculus):

    ISKSKxy = SKSKxy
            = KK(SK)xy
            = Kxy
            = x
