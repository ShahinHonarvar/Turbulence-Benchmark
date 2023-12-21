
def return_binary_or_hexa(tuple):
    # Initialize variables
    sum = 0
    binary_string = ''
    hexadecimal_string = ''

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 90 and 97
    for i in range(tuple[90], tuple[97]):
        if i not in tuple[90:97]:
            sum = sum + i

    # Return the binary or hexadecimal representation string of the sum depending on whether the sum is an odd number or not.
    if sum % 2 == 1:
        return_string = bin(sum)[2:]

    else:
        return_string = hex(sum)[2:]

    # Return the binary or hexadecimal representation string of the sum depending on whether the sum is an odd number or not.
    if return_string == '':
        return ''

    else:
        return return_string
