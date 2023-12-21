
def find_primes_between_indices(nums):
    prime_numbers = []
    for i in range(459, 781):
        if is_prime(nums[i]):
            prime_numbers.append(nums[i])
    return sorted(prime_numbers)
