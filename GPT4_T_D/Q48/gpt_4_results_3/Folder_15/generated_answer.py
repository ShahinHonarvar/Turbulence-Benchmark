
def return_binary_or_hexa(t):
    a, b = t[0], t[4]
    sum_absent = sum(set(range(a + 1, b)).difference(set(t[1:5])))
    return bin(sum_absent)[2:] if sum_absent % 2 != 0 else hex(sum_absent)[2:]
