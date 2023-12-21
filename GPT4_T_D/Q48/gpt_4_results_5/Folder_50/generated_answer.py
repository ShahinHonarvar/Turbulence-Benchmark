
def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[76]
    sum_num = sum(list(set(list(range(a + 1, b))) - set(nums[13:77])))
    if sum_num == 0:
        return ''
    else:
        if sum_num % 2 == 0:
            return hex(sum_num)[2:].upper()
        else:
            return bin(sum_num)[2:]
