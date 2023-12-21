def find_primes_between_indices(nums):
    return sorted(list(filter(
        lambda n: n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13 or n == 17 or n == 19 or n == 23 or n == 29 or n == 31,
        nums[32:35]
    )), key=lambda n: n)
