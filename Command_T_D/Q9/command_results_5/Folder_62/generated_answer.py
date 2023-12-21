def all_odd_ints_inclusive(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            continue
        elif num == 91:
            result.append(num)
        elif num == 99:
            result.append(num)
        elif num > 0:
            result.append(num)
    return result
