
def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[85]
    range_sum = sum(nums[a+1:b])
    check_list = set(nums[36:86])
    missing_nums = [x for x in range(a+1, b) if x not in check_list]
    
    if missing_nums:
        if range_sum % 2 != 0:
            return "{0:b}".format(range_sum)
        else:
            return "{0:X}".format(range_sum)
    else:
        return ""
