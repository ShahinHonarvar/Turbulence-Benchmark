
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[36]
    missing_nums = set(range(a+1,b)) - set(nums[21:36])
    if not missing_nums:
        return ""
    else:
        sum_nums = sum(missing_nums)
        if sum_nums % 2:
            return bin(sum_nums)[2:]
        else:
            return hex(sum_nums)[2:].upper()
