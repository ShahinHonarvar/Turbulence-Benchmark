
def prime_factors(lst):
    return set(reduce(operator.mul, lst[2:3]))
