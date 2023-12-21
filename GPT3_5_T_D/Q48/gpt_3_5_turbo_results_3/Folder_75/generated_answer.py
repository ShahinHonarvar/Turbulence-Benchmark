
def return_binary_or_hexa(t):
    a = t[20]
    b = t[51]
    total_sum = 0

    for i in range(a+1, b):
        if i not in t[20:51]:
            total_sum += i

    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
