
def if_decimal_is_divisible(binary_repr: str) -> bool:
    # Convert binary representation to decimal integer
    decimal = int(binary_repr, 2)

    # Calculate the 6th number that occurs in the Fibonacci sequence
    fibonacci = [0] + [0, 1]
    for i in range(2, 5):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    divisor = fibonacci[6]

    # Check if the decimal integer is divisible by the divisor
    return decimal % divisor == 0
