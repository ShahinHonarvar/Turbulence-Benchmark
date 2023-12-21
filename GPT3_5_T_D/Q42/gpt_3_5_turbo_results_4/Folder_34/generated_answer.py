
def prime_factors(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = lst[97]
    factors = set()
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            factors.add(divisor)
            num = num // divisor
        else:
            divisor += 1
    return factors
