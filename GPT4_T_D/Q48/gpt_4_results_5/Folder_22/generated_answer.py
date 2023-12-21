
def return_binary_or_hexa(nums):
    a = nums[40]
    b = nums[200]
    all_nums = set(range(a+1, b))
    existing_nums = set(nums[40:201])
    missing_nums = all_nums - existing_nums
    sum_nums = sum(missing_nums)
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
    return ''
