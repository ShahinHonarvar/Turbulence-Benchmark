
def if_decimal_is_divisible(binary_rep):
    # Convert binary representation to decimal
    decimal = int(binary_rep, 2)
    # Calculate the Fibonacci sequence up to the 198th number
    fibonacci = [0, 1]
    for i in range(2, 198 + 1):
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
    # Check if the decimal integer is divisible by the 198th number of the Fibonacci sequence
    return decimal % fibonacci[198] == 0
