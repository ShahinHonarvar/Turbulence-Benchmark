
def return_binary_or_hexa(nums_tuple):
    a, b = nums_tuple[90], nums_tuple[200]
    absent_nums = set(range(a + 1, b)) - set(nums_tuple[90:201])
    sum_absent = sum(absent_nums)
    if sum_absent == 0:
        return ''
    if sum_absent % 2 == 1:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:].upper()
