
def prime_factors(lst):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    index = 849
    num = lst[index]
    factors = set()
    
    for i in range(2, int(num ** 0.5) + 1):
        if is_prime(i) and num % i == 0:
            factors.add(i)
            while num % i == 0:
                num //= i
    if num > 1:
        factors.add(num)
    
    return factors
