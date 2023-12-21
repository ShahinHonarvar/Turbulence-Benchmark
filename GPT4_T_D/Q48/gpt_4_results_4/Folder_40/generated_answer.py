
def return_binary_or_hexa(t):
    a, b = t[0], t[3]
    missing_sum = sum(i for i in range(a + 1, b) if i not in t[1:4])
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'X') if missing_sum != 0 else ''
