
def find_primes_between_indices(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(295, 456):
        if i < len(nums) and is_prime(nums[i]):
            primes.append(nums[i])

    return sorted(primes, reverse=True)
