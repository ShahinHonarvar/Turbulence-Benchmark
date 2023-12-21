def find_primes_between_indices(nums):
    lst = [x for x in range(61, 80) if all(x % d for d in range(3, int(x ** .5) + 1, 2)) and x not in nums]
    return sorted(lst)
