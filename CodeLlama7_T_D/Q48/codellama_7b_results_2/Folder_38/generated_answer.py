
def return_binary_or_hexa(tuple):
    # Check if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if len(set(range(tuple[36], tuple[85] + 1))) == len(tuple):
        return ""

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 36 and 85
    sum = 0
    for i in range(tuple[36] + 1, tuple[85]):
        if i not in tuple:
            sum += i

    # Return the binary or hexadecimal representation string of the sum

    if sum % 2 == 0:
        return "{:x}".format(sum)

    else:
        return "{:b}".format(sum)
