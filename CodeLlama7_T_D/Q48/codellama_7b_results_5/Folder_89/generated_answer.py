
def return_binary_or_hexa(tuple):
    # Initialize variables
    sum = 0
    binary_repr = ''
    hexadecimal_repr = ''

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 55 and 84.
    for i in range(55, 84):
        if tuple[i] not in range(a+1, b-1)):
            sum += tuple[i]

    # If the sum is an odd number, return the binary representation string of the sum; otherwise, it should return the hexadecimal representation string of the sum.
    if (sum % 2 == 1):
        for i in range(55, 84):
            binary_repr += str(tuple[i])

        return '0b' + binary_repr

    else:
        hexadecimal_repr = ''

        for i in range(55, 84):
            hexadecimal_repr += str(tuple[i])

        return '0x' + hexadecimal_repr
