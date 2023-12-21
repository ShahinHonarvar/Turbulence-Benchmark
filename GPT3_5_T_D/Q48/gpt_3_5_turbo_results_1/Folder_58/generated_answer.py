
def return_binary_or_hexa(nums):
    a = nums[275]
    b = nums[871]
    missing_nums = set(range(a + 1, b)) - set(nums[276:871])
    if missing_nums:
        sum_missing_nums = sum(missing_nums)
        if sum_missing_nums % 2 == 1:
            return bin(sum_missing_nums)[2:]
        else:
            return hex(sum_missing_nums)[2:].upper()
    else:
        return ""
