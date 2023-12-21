
def return_binary_or_hexa(tuple):
    # Initialize variables
    sum = 0
    binary = ""
    hexadecimal = ""

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 3 and 9.
    for i in range(tuple[3] + 1, tuple[9] - 1):
        if i not in tuple:
            sum += i

    # Return an empty string if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple.
    if sum == 0:
        return ""

    # If the sum is an odd number, return the binary representation string of the sum. Otherwise, return the hexadecimal representation string of the sum.
    elif sum % 2 != 0:
        return str(bin(sum))[2:]
    else:
        return str(hex(sum))[2:]
