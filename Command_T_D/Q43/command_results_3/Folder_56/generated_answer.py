def find_primes_between_indices(nums):
    lst = []
    for i in range(40, 68):
        if all(nums[i] % d != 0 for d in range(3, int(nums[i] ** .5) + 1)):
            lst.append(nums[i])
    return sorted(lst, reverse=True)
