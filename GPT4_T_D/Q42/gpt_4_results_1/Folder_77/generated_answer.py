
def prime_factors(numbers):
    def factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return set(factors)

    if len(numbers) > 985:
        return factors(numbers[985])
    else:
        return "Index out of range"
