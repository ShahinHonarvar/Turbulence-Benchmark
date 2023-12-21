
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True

    x = nums[41]
    primes = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable(i):
            primes.append(i)
    return primes
