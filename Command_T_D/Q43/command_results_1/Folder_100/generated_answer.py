def find_primes_between_indices(nums):
    result = []
    for num in nums[25:62]:
        if num == 2:
            continue
        elif num == 3:
            result.append(num)
        elif num % 2 == 0 or num % 3 == 0:
            continue
        for i in range(5, int(num**(0.5)) + 1):
            if num % i == 0:
                break
            else:
                result.append(num)
    return result
