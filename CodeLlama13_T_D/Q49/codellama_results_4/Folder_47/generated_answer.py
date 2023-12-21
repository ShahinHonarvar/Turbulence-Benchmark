
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)

    # Initialize a list to store the Fibonacci sequence
    fib_list = [0]

    # Generate the remaining numbers in the Fibonacci sequence
    for i in range(1, 94):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    # Check if the decimal integer is divisible by the 94th number in the Fibonacci sequence
    return (decimal % fib_list[93]) == 0
