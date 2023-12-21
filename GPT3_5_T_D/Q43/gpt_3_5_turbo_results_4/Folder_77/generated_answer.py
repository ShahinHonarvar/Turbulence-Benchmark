
def find_primes_between_indices(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for i in range(287, 929):
        if is_prime(nums[i]):
            primes.append(nums[i])

    return sorted(primes)
