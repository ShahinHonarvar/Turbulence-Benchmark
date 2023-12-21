
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)

    # Generating the 175th number in the Fibonacci sequence
    num1, num2 = 0, 1
    fib_num = 0
    for _ in range(175):
        fib_num = num1 + num2
        num1, num2 = num2, fib_num

    return decimal_number % fib_num == 0
