
def prime_factors(nums):
    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f += 6
        return True    

    def factorize(n):
        factors = set()
        for x in range(2, int(n ** 0.5) + 1):
            while n % x == 0:
                if is_prime(x):
                    factors.add(x)
                n = n // x
        if n > 1:
            factors.add(n)
        return factors

    if len(nums) > 453:
        return factorize(nums[453])
    else:
        return set()
