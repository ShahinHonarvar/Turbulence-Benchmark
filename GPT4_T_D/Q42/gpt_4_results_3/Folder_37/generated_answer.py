
def prime_factors(numbers):
    if len(numbers) < 29:
        return "The list doesn't contain 29 elements."
    else:
        n = numbers[28]
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
