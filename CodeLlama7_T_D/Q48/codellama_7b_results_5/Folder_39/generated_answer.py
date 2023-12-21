
def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[44]
    b = tuple[91]
    sum = 0
    binary = ""
    hexa = ""

    # Calculate the sum of all integers from a + 1 to b - 1 that are not present in the tuple between indices 44 and 91
    for i in range(a + 1, b):
        if i not in tuple[44:91]:
            sum += i

    # If the sum is an odd number, return the binary representation string of the sum; otherwise, it should return the hexadecimal representation string of the sum.
    if sum % 2 == 0:
        hexa = f"{sum:X}"

    else:

        binary = f"{sum:b}"

    # Return an empty string if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple.
    if len(tuple[44:91]) == b - a - 1:
        return ""

    # Otherwise, return either the binary or hexadecimal representation string of the sum depending on whether it is an odd or even number.
    else:

        return binary if sum % 2 == 1 else hexa
