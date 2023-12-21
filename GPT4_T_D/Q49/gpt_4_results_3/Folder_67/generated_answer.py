
def if_decimal_is_divisible(binary_string):
    fibo_numbers = [0, 1]
    i = 2
    while len(fibo_numbers) < 108:
        fibo_numbers.append(fibo_numbers[i-1] + fibo_numbers[i-2])
        i+=1
    fibonacci_107 = fibo_numbers[-1]
    decimal_number = int(binary_string, 2)
    if decimal_number % fibonacci_107 == 0:
        return True
    else:
        return False
