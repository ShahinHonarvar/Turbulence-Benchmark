def all_right_truncatable_prime(nums):
    # This function should return the sorted list of all right-truncatable prime numbers less than x.
    # The returned list should be sorted in ascending order. If there is no such right-truncatable prime number, the function should return an empty list. A right-truncatable prime number is a prime number that remains prime when the last rightmost digit is successively removed.
    return sorted(nums for num in nums if all(nums[i] % 10 != d for i in range(len(nums) - 1) for d in range(10)))
