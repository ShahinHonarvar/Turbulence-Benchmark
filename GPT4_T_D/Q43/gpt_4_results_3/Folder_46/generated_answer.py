
def find_primes_between_indices(nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = [num for num in nums[20:26] if is_prime(num)]
    primes.sort(reverse=True)
    return primes
