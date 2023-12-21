
def prime_factors(lst):
    num = lst[2]
    factors = set()

    # Check for divisible prime factors starting from 2
    for i in range(2, num+1):
        while num % i == 0:
            factors.add(i)
            num //= i

    return factors
