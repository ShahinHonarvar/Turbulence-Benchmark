
def return_binary_or_hexa(nums):
    a = nums[34]
    b = nums[69]
    missing_nums = set(range(a + 1, b)) - set(nums[34:70])
    summed = sum(missing_nums)
    if summed % 2 != 0:
        return str(bin(summed))[2:]
    else:
        return str(hex(summed))[2:].upper()
