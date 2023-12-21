
def if_decimal_is_divisible(bin_rep):
    # fibonacci numbers
    a, b = 0, 1
    for _ in range(90):
        a, b = b, a + b

    decimal_num = int(bin_rep, 2)
    
    return decimal_num % a == 0
