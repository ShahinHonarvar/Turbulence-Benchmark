 
def find_primes_between_indices(nums):
    primes = sorted(nums[130:815])
    for p in primes:
        if nums[p] == p:
            break
    else:
        return []
    return primes
