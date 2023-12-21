
def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[79]
    omitted_nums_sum = sum(i for i in range(a + 1, b) if i not in tup[10:80])
    if omitted_nums_sum == 0:
        return ''
    elif omitted_nums_sum % 2 == 0:
        return hex(omitted_nums_sum)[2:]
    else:
        return bin(omitted_nums_sum)[2:]
