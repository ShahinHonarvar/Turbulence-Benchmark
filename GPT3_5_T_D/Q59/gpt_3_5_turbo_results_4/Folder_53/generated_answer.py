
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        n = str(n)
        while len(n) > 1:
            n = n[1:]
            if not is_prime(int(n)):
                return False
        return True

    x = nums[86]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)

    return sorted(left_truncatable_primes, reverse=True)
