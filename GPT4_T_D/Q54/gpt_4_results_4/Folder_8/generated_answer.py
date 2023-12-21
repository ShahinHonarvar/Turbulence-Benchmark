
def all_right_truncatable_prime(nums):
    x = nums[41]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            n //= 10
            if n > 0 and not is_prime(n):
                return False
        return True

    primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            primes.append(i)

    return sorted(primes, reverse=True)
