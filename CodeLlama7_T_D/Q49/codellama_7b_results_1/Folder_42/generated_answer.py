
def if_decimal_is_divisible(binary_rep):
    # Convert binary representation to decimal
    decimal = int(binary_rep, 2)
    # Calculate the 146th Fibonacci number
    fibonacci = [0, 1]
    for i in range(145):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    # Check if decimal is divisible by the 146th Fibonacci number
    return decimal % fibonacci[145] == 0
