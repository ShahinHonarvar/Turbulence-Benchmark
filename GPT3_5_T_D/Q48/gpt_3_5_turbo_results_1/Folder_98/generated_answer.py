
def return_binary_or_hexa(nums):
    a = nums[6]
    b = nums[7]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[6:8]]
    if len(missing_nums) == 0:
        return ''
    else:
        sum_nums = sum(missing_nums)
        if sum_nums % 2 == 0:
            return hex(sum_nums)[2:]
        else:
            return bin(sum_nums)[2:]
