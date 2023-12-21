
def return_binary_or_hexa(tuple):
    # Initialize variables
    sum = 0
    binary = ""
    hexa = ""

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 35 and 64
    for i in range(tuple[35] + 1, tuple[64] - 1):
        if i not in tuple:
            sum += i

    # Return the binary or hexadecimal representation string of the sum, depending on whether it is an odd number
    if sum % 2 == 0:
        return hexa
    else:
        return binary
