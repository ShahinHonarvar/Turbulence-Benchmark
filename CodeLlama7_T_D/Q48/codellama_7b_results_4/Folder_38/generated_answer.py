 def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[36]
    b = tuple[85]
    sum = 0
    binary_representation = ''
    hexadecimal_representation = ''

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 36 and 85
    for i in range(a + 1, b):
        if i not in tuple[36:85]:
            sum += i

    # If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum
    if sum % 2 == 1:
        for digit in bin(sum)[2:]:
            binary_representation += digit

    else:

        for digit in hex(sum)[2:]:
            hexadecimal_representation += digit

    # Return an empty string if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if binary_representation == '' and hexadecimal_representation == '':
        return ''

    # Otherwise, return the binary or hexadecimal representation string of the sum
    else:

        return binary_representation if binary_representation != '' else hexadecimal_representation
