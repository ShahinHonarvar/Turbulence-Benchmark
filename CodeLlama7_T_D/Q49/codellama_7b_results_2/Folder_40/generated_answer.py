 def if_decimal_is_divisible(binary_repr: str) -> bool:
    # Convert binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Find the first occurrence of 4 in the Fibonacci sequence
    for i in range(decimal_int + 1):
        if str(i).count('4') > 0:
            # If the number is divisible by the 4th number in the Fibonacci sequence, return True
            if decimal_int % i == 0:
                return True

    # If the number is not divisible by any of the numbers in the Fibonacci sequence, return False
    return False
