 def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[16]
    b = tuple[87]
    sum = 0
    binary_string = ''
    hexadecimal_string = ''

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 16 and 87
    for i in range(a+1, b):
        if i not in tuple[16:87]:
            sum += i

    # Return the binary representation string of the sum if it is an odd number
    # Otherwise, return the hexadecimal representation string of the sum
    if sum % 2 == 0:
        for digit in bin(sum)[2:]:
            binary_string += digit

        return binary_string[1:]

    else:

        for digit in hex(sum)[2:]:
            hexadecimal_string += digit

        return hexadecimal_string.lower()
