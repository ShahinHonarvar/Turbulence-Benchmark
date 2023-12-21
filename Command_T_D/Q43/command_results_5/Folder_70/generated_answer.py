def find_primes_between_indices(nums):
    return sorted(set(nums) for num in nums if all(num % i != 0 for i in range(2, int(num**(0.5)) + 1)))
