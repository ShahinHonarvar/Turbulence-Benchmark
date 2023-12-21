
def return_binary_or_hexa(tuple):
    a, b = tuple[15], tuple[57]
    sum = 0
    for i in range(a+1, b-1):
        if i not in tuple:
            sum += 1
    if sum % 2 == 0:
        return hex(sum)
    else:
        binary_str = bin(sum)[2:]
        if binary_str[0] == '0':
            return binary_str[1:]
        else:
            return binary_str
