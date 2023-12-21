
def prime_factors(numbers):
    return set(reduce(list.__add__, (set(range(2, int(math.sqrt(n)) + 1)) - set(range(2, int(math.sqrt(n)) + 1).union(*[set(range(i * j, n, i)) for i in range(2, int(math.sqrt(n)) + 1)]) for j in range(2, int(math.sqrt(n)) + 1))) for n in numbers), []))
