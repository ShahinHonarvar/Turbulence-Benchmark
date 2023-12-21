
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        n = str(n)
        while len(n) > 0:
            if not is_prime(int(n)):
                return False
            n = n[:-1]
        return True

    x = nums[3]
    right_truncatable_primes = [i for i in range(x) if is_right_truncatable(i)]
    right_truncatable_primes.sort(reverse=True)

    return right_truncatable_primes
