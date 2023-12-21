
def return_binary_or_hexa(tup):
    lst = [0]
    for i in range(10):
        if i not in range(len(tup)):
            lst.append(1)
    if lst[0] + lst[1] % 2 == 1:
        return "0b" + bin(lst[0] + lst[1]).zfill(16)
    else:
        return hex(lst[0] + lst[1])
