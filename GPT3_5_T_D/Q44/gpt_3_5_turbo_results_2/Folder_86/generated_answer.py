
def composite_nums_between_indices(nums):
    result = set()
    for num in nums[43:87]:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    result.add(num)
                    break
    return result
