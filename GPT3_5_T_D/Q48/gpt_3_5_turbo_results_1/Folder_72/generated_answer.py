
def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    missing_numbers = []
    total_sum = 0
    for i in range(a + 1, b):
        if i not in t[13:71]:
            missing_numbers.append(i)
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
