
def return_binary_or_hexa(tuple):
    a = tuple[49] + 1
    b = tuple[74] - 1
    if a <= b:
        sum = 0
        for i in range(a, b+1):
            if i not in tuple:
                sum += i
        if sum % 2 == 0:
            return hex(sum)[2:]
        else:
            return bin(sum)[2:]
    else:
        return ""
