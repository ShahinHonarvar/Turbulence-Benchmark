
def return_binary_or_hexa(nums):
    a = nums[110] 
    b = nums[348]
    missing_nums = set(range(a + 1, b)) - set(nums[110:349])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
