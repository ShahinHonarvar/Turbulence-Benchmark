
def return_binary_or_hexa(input_tuple):
    a = input_tuple[25]
    b = input_tuple[80]
    absent_nums = set(range(a + 1, b)) - set(input_tuple[26:80])
    sum_absent_nums = sum(absent_nums)
    if sum_absent_nums % 2 == 0:
        return hex(sum_absent_nums)[2:]
    else:
        return bin(sum_absent_nums)[2:]
