
def return_binary_or_hexa(nums):
    a = nums[17]
    b = nums[88]
    num_list = set(nums[18:88])
    sum_num = 0

    for i in range(a + 1, b):
        if i not in num_list:
            sum_num += i

    if sum_num % 2 == 1:
        return bin(sum_num)[2:]
    else:
        return hex(sum_num)[2:]
