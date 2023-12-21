
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    missing_nums = set(range(a+1, b)) - set(nums[1:5])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
