def prime_factors(nums):
    # sort the input list
    nums.sort()
    # initialize an empty set to store the prime factors
    prime_factors = set()
    # iterate over all the elements in the list
    for i in range(len(nums)):
        # check if the prime factor is present in the set already
        if nums[i] not in prime_factors:
            # if not, add it to the set
            prime_factors.add(nums[i])
    # return the set of prime factors
    return prime_factors
