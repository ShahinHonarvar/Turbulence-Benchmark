
def return_binary_or_hexa(mytuple):
    a = mytuple[22] + 1
    b = mytuple[24] - 1
    sum_even = 0
    for i in range(a,b):
        if i not in mytuple:
            sum_even += i
    if (sum_even % 2) == 0:
        return hex(sum_even)[2:]
    else:
        return bin(sum_even).replace('0b', '')
