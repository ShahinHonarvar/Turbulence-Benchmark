
def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[81]
    missing_nums = [x for x in range(a+1, b) if x not in nums[38:82]]
    if len(missing_nums) == 0:
        return ""
    else:
        total = sum(missing_nums)
        if total % 2 == 0:
            return hex(total)[2:]
        else:
            return bin(total)[2:]
