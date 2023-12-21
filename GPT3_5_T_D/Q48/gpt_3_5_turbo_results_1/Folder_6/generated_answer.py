
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[93]
    missing_nums = [x for x in range(a+1, b) if x not in nums[20:94]]
    if len(missing_nums) == 0:
        return ""
    else:
        total_sum = sum(missing_nums)
        if total_sum % 2 == 0:
            return hex(total_sum)[2:]
        else:
            return bin(total_sum)[2:]
