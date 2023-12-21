
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[3]
    missing_nums = [x for x in range(a+1, b) if x not in nums]
    if missing_nums:
        result = sum(missing_nums)
        if result % 2 != 0:
            return bin(result)[2:]
        else:
            return hex(result)[2:]
    else:
        return ""
