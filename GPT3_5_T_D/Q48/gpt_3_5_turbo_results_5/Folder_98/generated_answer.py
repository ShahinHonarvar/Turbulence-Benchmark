
def return_binary_or_hexa(nums):
    a = nums[6]
    b = nums[7]
    if b - a <= 1:
        return ''
    sum_nums = 0
    for i in range(a + 1, b):
        if i not in nums[6:8]:
            sum_nums += i
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:]
