
def if_decimal_is_divisible(bin_string):
    # Fibonacci Sequence at 40th position
    fib_40 = 63245986
    
    dec_value = int(bin_string, 2)

    if dec_value % fib_40 == 0:
        return True
    else:
        return False
