 
def find_primes_between_indices(nums):
    result = []
    for i in range(69, 80+1):
        if all(nums[i] % k for k in range(2, int(nums[i**0.5])+1)):
            result.append(nums[i])
    return sorted(result)
