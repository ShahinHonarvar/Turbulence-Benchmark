
def return_binary_or_hexa(arg):
    a = arg[0]
    b = arg[2]

    sum_num = sum(set(range(a + 1, b)) - set(arg[1:3]))

    if sum_num % 2 == 0:
        return hex(sum_num)[2:]
    else:
        return bin(sum_num)[2:]
