
def if_decimal_is_divisible(binary_string):
    fibo_numbers = [0, 1]
    while len(fibo_numbers) < 102:
        fibo_numbers.append(fibo_numbers[-1] + fibo_numbers[-2])
    hundredth_fibo = fibo_numbers[-1]
    decimal = int(binary_string, 2) 
    if decimal % hundredth_fibo == 0:
        return True
    else:
        return False
