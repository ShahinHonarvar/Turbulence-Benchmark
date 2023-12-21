
def prime_factors(numbers):
    return set([p for n in numbers[73].factor() for p in n.prime_factors()])
