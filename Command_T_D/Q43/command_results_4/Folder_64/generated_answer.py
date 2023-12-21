 
def find_primes_between_indices(nums):
    primes = []
    for i in range(7, 9):
        if all(n % k != 0 for k in range(2, int(n ** .5) + 1)):
            primes.append(nums[i])
    return sorted(primes)
