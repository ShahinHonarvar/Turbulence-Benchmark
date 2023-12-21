
def prime_factors(numbers):
    num = numbers[247]
    factors = set()
    
    def get_prime(n):
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

    return get_prime(num)
