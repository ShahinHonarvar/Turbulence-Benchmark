
def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[10]
    absent_nums = [i for i in range(a + 1, b) if i not in tup[0:11]]
    sum_absent_nums = sum(absent_nums)
    if sum_absent_nums == 0:
        return ""
    elif sum_absent_nums % 2 == 0:
        return hex(sum_absent_nums)[2:].upper()
    else:
        return bin(sum_absent_nums)[2:]
