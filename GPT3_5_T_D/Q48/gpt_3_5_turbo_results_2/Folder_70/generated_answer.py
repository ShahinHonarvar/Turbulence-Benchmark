
def return_binary_or_hexa(nums):
    a = nums[43]
    b = nums[70]
    
    missing_nums = [x for x in range(a + 1, b) if x not in nums[43:71]]
    if len(missing_nums) == 0:
        return ""

    sum_nums = sum(missing_nums)
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()
