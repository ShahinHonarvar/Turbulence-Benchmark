
def return_binary_or_hexa(t):
    a = t[2]
    b = t[8]
    sum_num = 0
    missing_nums = set(range(a + 1, b)) - set(t[2:9])
    for num in missing_nums:
        sum_num += num
    if sum_num == 0:
        return ''
    elif sum_num % 2 == 0:
        return hex(sum_num)[2:]
    else:
        return bin(sum_num)[2:]
