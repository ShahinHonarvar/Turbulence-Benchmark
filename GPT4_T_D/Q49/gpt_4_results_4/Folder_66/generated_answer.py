
def if_decimal_is_divisible(binary_repr):
    decimal_number = int(binary_repr, 2)
    
    # Get the 120th Fibonacci number
    fib_numbers = [0, 1]
    for i in range(2, 120):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
    fib_120 = fib_numbers[-1]

    return decimal_number % fib_120 == 0
