 def return_binary_or_hexa(tuple):
    # initialize variables
    a = tuple[2]
    b = tuple[8]
    sum = 0
    binary_representation = ''
    hexadecimal_representation = ''
    # calculate the sum of all integers from a + 1 to b - 1 that are not present in the tuple between indices 2 and 8
    for i in range(a + 1, b):
        if i not in tuple[2:8]:
            sum += i

    # return the binary representation of the sum if it is an odd number; otherwise, return the hexadecimal representation of the sum
    if sum % 2 != 0:
        for digit in bin(sum)[2:]:
            binary_representation += digit

        return binary_representation

    else:

        for digit in hex(sum)[2:]:
            hexadecimal_representation += digit

        return hexadecimal_representation
