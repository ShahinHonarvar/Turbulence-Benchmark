
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    missing_nums = set(range(a+1, b)) - set(nums[1:4])
    sum_nums = sum(missing_nums)

    if sum_nums % 2 != 0:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()
