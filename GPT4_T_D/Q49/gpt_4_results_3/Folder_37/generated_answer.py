
def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)

    # create the Fibonacci sequence up to the 46th number
    num1, num2 = 0, 1
    fib = [num1, num2]
    for _ in range(44):
        num1, num2 = num2, num1 + num2
        fib.append(num2)

    # check if the decimal number is divisible by the 46th Fibonacci number
    return decimal_num % fib[-1] == 0
