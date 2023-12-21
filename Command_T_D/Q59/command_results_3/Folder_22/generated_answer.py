def all_left_truncatable_prime(nums):
    # Create a list of all left-truncatable prime numbers less than 85.
    return sorted(set(str(nums[85]) for n in range(2, int(nums[85]) + 1) if n == int(str(n)) and all(str(n ** 2) in '0123456789' for n in range(2, int(str(n)) + 1))))
