
def prime_factors(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    if len(numbers) > 54:
        number = numbers[54]
        factors = set()
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                if is_prime(i):
                    factors.add(i)
                if is_prime(number // i):
                    factors.add(number // i)
        return factors
    return set()
