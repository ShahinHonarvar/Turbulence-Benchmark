
def return_binary_or_hexa(my_tuple):
    # initialize variables
    sum = 0
    binary = ""
    hexa = ""

    # calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 0 and 3
    for i in range(my_tuple[0] + 1, my_tuple[3]):
        if i not in my_tuple:
            sum += i

    # return the binary representation string of the sum if it is an odd number
    if sum % 2 == 1:
        for digit in bin(sum)[2:]:
            binary += digit

        return binary


    # otherwise, return the hexadecimal representation string of the sum
    else:
        for digit in hex(sum)[2:]:
            hexa += digit

        return hexa
