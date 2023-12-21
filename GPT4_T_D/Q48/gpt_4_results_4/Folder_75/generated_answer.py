
def return_binary_or_hexa(num_tuple):
    a, b = num_tuple[20], num_tuple[51]
    absent_nums = set(range(a+1, b)) - set(num_tuple[21:51])
    sum_absent_nums = sum(absent_nums)
    if sum_absent_nums % 2 != 0:
        return bin(sum_absent_nums)[2:]
    else:
        return hex(sum_absent_nums)[2:].upper()
