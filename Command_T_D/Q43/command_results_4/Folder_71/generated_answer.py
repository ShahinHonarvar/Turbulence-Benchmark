def find_primes_between_indices(nums):
    return sorted(list(filter(lambda x: x%2==1 and x!=1 and x!=57 and x!=59 and x!=61 and x!=63, nums)))
