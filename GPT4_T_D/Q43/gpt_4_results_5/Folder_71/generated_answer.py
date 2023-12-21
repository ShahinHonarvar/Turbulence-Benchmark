
def find_primes_between_indices(nums):
    nums = nums[57:65]
    primes = [x for x in nums if all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x != 1 and x != 0]
    return sorted(primes, reverse=True)
