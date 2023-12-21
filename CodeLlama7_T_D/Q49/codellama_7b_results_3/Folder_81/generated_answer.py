
def if_decimal_is_divisible(binary_str):
    # Convert the binary string to an integer
    num = int(binary_str, 2)
    # Calculate the remainder of dividing the number by 97
    rem = num % 97
    # If the remainder is 0, then the number is divisible by 97
    if rem == 0:
        return True

    # Otherwise, return False

    return False
