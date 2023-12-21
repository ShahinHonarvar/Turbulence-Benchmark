
def find_primes_between_indices(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    filtered_primes = [num for num in nums[1:2] if is_prime(num)]
    return sorted(filtered_primes)
