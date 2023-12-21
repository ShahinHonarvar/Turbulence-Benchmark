
def prime_factors(integers):
    if len(integers) <= 45:
        return set()
    else:
        n = integers[45]
        factors = []
        for i in range(2, int(n**0.5) + 1):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 1:
            factors.append(n)
        return set(factors)
