 
def find_primes_between_indices(nums):
    primes = []
    for i in range(31, 93):
        if all(nums[j] % i != 0 for j in range(i * 2, 93, i)):
            primes.append(i)
    return sorted(primes)
