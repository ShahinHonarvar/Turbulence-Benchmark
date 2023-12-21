
def return_binary_or_hexa(nums):
    a = nums[80]
    b = nums[200]
    num_list = set(nums[81:200])
    sum_nums = sum(i for i in range(a+1, b) if i not in num_list)
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
