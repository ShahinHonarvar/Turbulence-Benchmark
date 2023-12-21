
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True

    primes = []
    for num in range(2, nums[433]):
        if '0' not in str(num) and is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)
