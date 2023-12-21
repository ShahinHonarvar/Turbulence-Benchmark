def find_primes_between_indices(nums):
    lst = sorted(nums[23:75])
    primes = []
    for n in lst:
        if all(n % x for x in range(2, int(n ** .5) + 1)):
            primes.append(n)
    return primes
