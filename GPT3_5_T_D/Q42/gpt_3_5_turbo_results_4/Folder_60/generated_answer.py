
def prime_factors(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    num = arr[88]
    factors = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                factors.add(i)
            if is_prime(num // i):
                factors.add(num // i)
    return factors
