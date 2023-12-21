
def prime_factors(numbers):
    def factors(n):
        i = 2
        prime_factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                prime_factors.append(i)
        if n > 1:
            prime_factors.append(n)
        return set(prime_factors)

    if len(numbers) > 72:
        return factors(numbers[72])
    else:
        return "List has less than 73 elements"
