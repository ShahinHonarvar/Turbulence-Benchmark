
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[8]
    excluded_nums = set(nums[1:8])
    sum_nums = sum(i for i in range(a + 1, b) if i not in excluded_nums)
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:].upper()
    else:
        return bin(sum_nums)[2:]
