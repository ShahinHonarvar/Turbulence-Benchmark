
def prime_factors(numbers):
    def factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors

    if len(numbers) > 537:
        return factors(numbers[537])
    else:
        return "Index out of range"
