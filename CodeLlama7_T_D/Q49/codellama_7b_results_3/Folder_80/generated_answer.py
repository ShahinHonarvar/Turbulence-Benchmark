
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Find the first occurrence of the 179th Fibonacci number in the string
    fibonacci_number = 0
    for i in range(len(binary_string)):
        if binary_string[i] == "1":
            fibonacci_number += 1
            if fibonacci_number == 179:
                break

    # Check if the decimal integer is divisible by the Fibonacci number
    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False
