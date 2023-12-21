def find_primes_between_indices(nums):
    start, stop = nums[56], nums[57]
    primes = []
    for num in nums:
        if num == start:
            continue
        elif num == stop:
            break
        elif num > stop:
            return primes
        elif num < start:
            continue
        elif num % 2 == 0 or num % 3 == 0:
            continue
        elif all(num % d == 0 for d in range(5, int(num ** .5) + 1, 6)):
            continue
        elif num % 5 == 0:
            continue
        else:
            primes.append(num)
    return primes
