
def prime_factors(numbers):
    element = numbers[985]
    factors = set()
    i = 2
    while i * i <= element:
        if element % i:
            i += 1
        else:
            element //= i
            factors.add(i)
    if element > 1:
        factors.add(element)
    return factors
