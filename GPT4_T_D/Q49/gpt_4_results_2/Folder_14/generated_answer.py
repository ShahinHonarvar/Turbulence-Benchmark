
def if_decimal_is_divisible(binary_string):
    fib_number = [0, 1]
    for i in range(25):
        fib_number.append(fib_number[-1] + fib_number[-2])
    
    decimal = int(binary_string, 2)

    return decimal % fib_number[27] == 0
