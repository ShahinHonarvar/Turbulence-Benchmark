
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n in (2, 3):
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def is_right_truncatable_prime(n):
        n = str(n)
        while len(n) > 0:
            if not is_prime(int(n)):
                return False
            n = n[:-1]
        return True

    x = nums[71]
    primes = [n for n in range(1, x) if is_right_truncatable_prime(n)]
    primes.sort(reverse=True)
    return primes
