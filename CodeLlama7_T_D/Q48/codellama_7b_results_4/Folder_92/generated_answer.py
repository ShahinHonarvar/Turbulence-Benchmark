
def return_binary_or_hexa(tuple):
    # initialize variables
    sum = 0
    binary_string = ''
    hexadecimal_string = ''

    # calculate sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 0 and 2
    for i in range(tuple[0] + 1, tuple[2]):
        if i not in tuple:
            sum += i

    # return binary representation string of the sum if it is an odd number
    if sum % 2 == 1:
        for digit in bin(sum)[3:]:
            binary_string += digit

        return binary_string

    # return hexadecimal representation string of the sum otherwise
    else:
        for digit in hex(sum)[2:]:
            hexadecimal_string += digit

        return hexadecimal_string
