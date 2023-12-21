
def prime_factors(numbers):
    number = numbers[47]
    
    def factors(n):
        i = 2
        factors = []
        while i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        return set(factors)

    return factors(number)
