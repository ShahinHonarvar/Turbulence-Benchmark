def find_primes_between_indices(nums):
    start = nums.index(38)
    end = nums.index(55)
    primes = []
    for num in nums[start:end+1]:
        if num == 2 or num == 3:
            continue
        elif num == 1:
            break
        elif all(num % d == 0 for d in range(2, int(num**(0.5)) + 1)):
            break
        else:
            primes.append(num)
    return sorted(primes)[::-1] if primes else []
