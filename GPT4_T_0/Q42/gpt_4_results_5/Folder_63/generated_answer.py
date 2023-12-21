
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
        return factors

    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

    prime_factors = [i for i in factors(numbers[57]) if is_prime(i)]
    return set(prime_factors)
