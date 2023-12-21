
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True

    x = nums[73]
    truncatable_primes = []
    for i in range(2, x):
        if is_truncatable(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
