
def return_binary_or_hexa(nums):
    a = nums[40]
    b = nums[200]
    excluded_nums = set(nums[41:200])
    sum_nums = 0

    for i in range(a + 1, b):
        if i not in excluded_nums:
            sum_nums += i

    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:]
