def prime_factors(nums):
    if len(nums) == 0:
        return set()
    for i in range(len(nums)):
        num = nums[i]
        if num < 2:
            continue
        else:
            if num == 2 or num == 3:
                yield num
            else:
                if num % 2 == 0 or num % 3 == 0:
                    for j in range(5, int(num**(0.5)) + 1, 6):
                        if num % j == 0:
                            yield j
                            break
                else:
                    yield num
    return set()
