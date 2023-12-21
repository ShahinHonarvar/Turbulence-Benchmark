
def prime_factors(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = nums[91]
    factors = set()
    for i in range(2, num // 2 + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
    return factors
