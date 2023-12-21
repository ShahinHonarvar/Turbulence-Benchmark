
def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[200]
    missing_nums = set(range(a+1, b)) - set(nums[61:200])
    if len(missing_nums) == 0:
        return ''
    else:
        sum_missing_nums = sum(missing_nums)
        if sum_missing_nums % 2 == 1:
            return bin(sum_missing_nums)[2:]
        else:
            return hex(sum_missing_nums)[2:]
