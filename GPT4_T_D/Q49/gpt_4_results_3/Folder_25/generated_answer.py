
def if_decimal_is_divisible(binary_repr):
    # Convert binary to decimal
    decimal = int(binary_repr, 2)
    # Fibonacci sequence
    fibonacci = [0, 1]
    for _ in range(2, 19):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    # Return true if divisible, else false
    return decimal % fibonacci[-1] == 0
