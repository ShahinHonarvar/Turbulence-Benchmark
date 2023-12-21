import math
def composite_nums_between_indices(nums):
    result = set()
    for n in nums[25:87]:
        if n < 2 or n % 2 == 0 or n % 3 == 0:
            continue
        num = n**2
        if num == 1 or num == 4 or num == 6 or num == 9:
            continue
        sqrt_n = int(math.sqrt(n))
        for i in range(3, sqrt_n + 1):
            if n % i == 0:
                result.add(n)
                break
    return result
