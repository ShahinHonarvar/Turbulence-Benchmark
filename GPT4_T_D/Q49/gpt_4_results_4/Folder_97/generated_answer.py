
def if_decimal_is_divisible(bin_string):
    binary = bin_string
    decimal = int(binary, 2)

    n1, n2 = 0, 1
    count = 0
    fibo_num = 0

    while count < 114:
        fibo_num = n1 + n2
        n1 = n2
        n2 = fibo_num  
        count += 1

    if decimal % fibo_num == 0:
        return True
    else:
        return False
