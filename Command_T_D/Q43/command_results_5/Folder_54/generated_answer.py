def find_primes_between_indices(nums):
    start = next((el for el in nums if el == 13), None)
    end = next((el for el in nums if el == 63), None)
    if start and end:
        return sorted(list(filter(lambda x: all(x % d != 0 for d in range(2, int(x ** .5) + 1)), nums[start:end + 1])))
    else:
        return []
