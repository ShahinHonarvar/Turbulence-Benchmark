def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[10:100]:
        if not num % 100:
            continue
        result.append(num)
    return result
