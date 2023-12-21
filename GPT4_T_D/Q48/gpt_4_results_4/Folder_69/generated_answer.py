
def return_binary_or_hexa(t):
    a, b = t[39], t[43]
    total_sum = sum(i for i in range(a + 1, b) if i not in t[39:44])
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
