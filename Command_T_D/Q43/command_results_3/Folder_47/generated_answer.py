def find_primes_between_indices(nums):
    if len(nums) < 67:
        return []
    first_index = nums.index(2)
    last_index = nums.index(nums[-1])
    if last_index - first_index < 13:
        return []
    primes = nums[first_index:last_index + 1]
    primes = sorted(set(primes))
    return primes[::-1]
