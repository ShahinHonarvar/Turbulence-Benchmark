
def find_primes_between_indices(nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(61, 80):
        if i < len(nums) and is_prime(nums[i]):
            primes.append(nums[i])

    return sorted(primes)
