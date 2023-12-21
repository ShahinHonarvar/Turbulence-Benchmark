 
def find_primes_between_indices(nums):
    primes = []
    for i in range(2, len(nums) + 1):
        if all(nums[j] != i for j in range(i**2, len(nums) + 1, i)):
            primes.append(nums[i-1])
    return primes
