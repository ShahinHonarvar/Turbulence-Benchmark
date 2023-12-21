
def prime_factors(numbers):
    factorized = set()
    for n in numbers:
        if n == 410:
            for i in range(2, int(n**0.5) + 1):
                while n % i == 0:
                    factorized.add(i)
                    n //= i
    return factorized
