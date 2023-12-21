def find_primes_between_indices(nums):
    primes = []
    for num in nums[830:849]:
        if num == 1:
            continue
        elif num == 2 or num == 3:
            primes.append(num)
        elif num % 2 == 0 or num % 3 == 0:
            continue
        elif num < 2:
            continue
        else:
            primes.extend([num, num + 2, num + 3])
    return sorted(set(primes))
