
def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[44]
    missing_nums = [x for x in range(a+1, b) if x not in nums[32:44+1]]
    if len(missing_nums) == 0:
        return ''
    else:
        sum_missing_nums = sum(missing_nums)
        if sum_missing_nums % 2 == 0:
            return hex(sum_missing_nums)[2:]
        else:
            return bin(sum_missing_nums)[2:]
