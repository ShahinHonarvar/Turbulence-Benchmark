
def if_decimal_is_divisible(binary_string):
    fibo_numbers = [0, 1]
    for i in range(2, 16):
        next_number = fibo_numbers[i - 1] + fibo_numbers[i - 2]
        fibo_numbers.append(next_number)
    
    decimal_number = int(binary_string, 2)
    return decimal_number % fibo_numbers[15] == 0
