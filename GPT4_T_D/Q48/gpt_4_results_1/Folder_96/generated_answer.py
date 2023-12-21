
def return_binary_or_hexa(num_tuple):
    a = num_tuple[50]
    b = num_tuple[200]
    missing_nums = set(range(a + 1, b)) - set(num_tuple[50:201])
    sum_nums = sum(missing_nums)
    if sum_nums == 0:
        return ""
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:].upper()
    else:
        return bin(sum_nums)[2:]
