
def find_primes_between_indices(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in range(7, 10):
        if is_prime(nums[num]):
            primes.append(nums[num])
    return sorted(primes, reverse=True)
