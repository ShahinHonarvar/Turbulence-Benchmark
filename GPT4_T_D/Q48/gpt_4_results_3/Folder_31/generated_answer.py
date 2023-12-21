
def return_binary_or_hexa(nums):
    a = nums[33]
    b = nums[78]
    missing_nums = set(range(a + 1, b)) - set(nums[33:79])
    sum_nums = sum(missing_nums)
    if sum_nums == 0:
        return ''
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()
