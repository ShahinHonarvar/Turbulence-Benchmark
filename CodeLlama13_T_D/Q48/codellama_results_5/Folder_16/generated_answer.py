
def return_binary_or_hexa(tuple):
    a = tuple[90]
    b = tuple[97]
    sum = 0
    for i in range(a+1, b-1):
        if i not in tuple:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum).upper().replace("0X", "")
