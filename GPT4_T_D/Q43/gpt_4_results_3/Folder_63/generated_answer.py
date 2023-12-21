
def find_primes_between_indices(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_nums = [n for n in nums[28:37] if is_prime(n)]
    return sorted(prime_nums)
