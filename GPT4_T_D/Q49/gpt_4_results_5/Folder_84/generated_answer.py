
def if_decimal_is_divisible(binary_num):
    dec_num = int(binary_num, 2)
    fibonacci_number = 0
    a, b = 0, 1
    
    for i in range(196):
        fibonacci_number = a
        a, b = b, a + b

    return dec_num % fibonacci_number == 0
