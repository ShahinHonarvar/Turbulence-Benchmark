
def return_binary_or_hexa(tple):
    a, b = tple[48], tple[76]
    tple_range = tple[49:76]
    sum_num = sum(set(range(a + 1, b)) - set(tple_range))

    if sum_num == 0:
        return ""
    elif sum_num % 2 == 0:
        return hex(sum_num)[2:]
    else:
        return bin(sum_num)[2:]
