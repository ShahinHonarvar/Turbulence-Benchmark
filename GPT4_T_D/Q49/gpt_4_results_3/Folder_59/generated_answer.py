
def if_decimal_is_divisible(bin_str):
    decimal_rep = int(bin_str, 2)
    fibonacci_number = 2111485077978050
    return decimal_rep % fibonacci_number == 0
