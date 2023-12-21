
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Calculate the index of the 198th Fibonacci number in the sequence
    index = (198 - 1) // 2
    # Check if the decimal integer is divisible by the corresponding Fibonacci number
    return decimal_integer % fibonacci(index + 1) == 0
def fibonacci(n):
    # Base case: n = 1 or n = 2
    if n in [1, 2]:
        return 1

    # Recursive case: calculate the (n-1)th and (n-2)th Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
