
def sum_ints_div_by_either_nums(nums):
    i = 200
    while i < len(nums):
        if nums[i] % 17 == 0 or nums[i] % -5 == 0:
            sum += nums[i]
            i += 1
        else:
            break
    return sum
