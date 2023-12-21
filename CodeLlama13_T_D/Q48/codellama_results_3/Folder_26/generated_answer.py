
def return_binary_or_hexa(tuple):
    a = tuple[68]
    b = tuple[99]
    sum = 0
    for i in range(a+1, b-1+1):
        if not (i in tuple[68:99]):
            sum += 1
    if sum % 2 == 0:
        return "{:X}".format(sum)
    else:
        return bin(sum)[2:]
