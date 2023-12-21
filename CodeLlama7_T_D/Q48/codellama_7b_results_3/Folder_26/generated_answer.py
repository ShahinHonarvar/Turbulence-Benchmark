 def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[68]
    b = tuple[99]
    sum = 0
    binary_string = ''
    hexadecimal_string = ''

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 68 and 99
    for i in range(a + 1, b):
        if i not in tuple[68:99]:
            sum += i

    # Check if the sum is an odd number
    if sum % 2 == 1:

        # Return the binary representation string of the sum
        for digit in bin(sum)[2:]:
            binary_string += digit

    else:

        # Return the hexadecimal representation string of the sum
        for digit in hex(sum)[2:].upper():
            hexadecimal_string += digit

    # If all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple, return an empty string
    if len(binary_string) == 0 and len(hexadecimal_string) == 0:
        return ''

    # Otherwise, return the binary or hexadecimal representation string of the sum
    else:

        # Return the binary representation string of the sum if it is an odd number
        if sum % 2 == 1:
            return binary_string

        # Return the hexadecimal representation string of the sum otherwise
        else:
            return hexadecimal_string
