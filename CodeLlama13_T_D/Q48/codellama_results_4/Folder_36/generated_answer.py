
def return_binary_or_hexa(mytuple):
    a = mytuple[110]
    b = mytuple[348]
    sum_of_ints = 0
    for i in range(a+1, b):
        if i not in mytuple:
            sum_of_ints += i
    if sum_of_ints % 2 == 0:
        return hex(sum_of_ints)
    else:
        binary = bin(sum_of_ints)[2:]
        return binary.zfill(8)
