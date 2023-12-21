
def prime_factors(numbers):
    if len(numbers) <= 94:
        return set()

    def factors(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors

    return factors(numbers[94])
