
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 36 and 54.
    sum = 0
    for i in range(36, 54):
        if my_tuple[i] not in range(my_tuple[36] + 1, my_tuple[54] - 1)):
            sum += my_tuple[i]
    # Return the binary or hexadecimal representation string of the sum.
    if sum % 2 == 0:
        return "{:x}".format(sum)
    else:
        return "{:b}".format(sum)
