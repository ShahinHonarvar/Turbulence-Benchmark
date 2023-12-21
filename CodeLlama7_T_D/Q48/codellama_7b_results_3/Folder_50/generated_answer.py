
def return_binary_or_hexa(tuple):
    # Check if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    present = True
    for i in range(len(tuple)):
        if tuple[i] not in range(tuple[13] + 1, tuple[76] - 1):
            present = False
            break

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 13 and 76
    if present:
        return ""

    else:

        sum = 0

        for i in range(len(tuple)):
            if tuple[i] not in range(tuple[13] + 1, tuple[76] - 1):
                sum += tuple[i]

        # Return the binary or hexadecimal representation string of the sum
        if sum % 2 == 0:
            return "{:x}".format(sum)

        else:

            return "{:b}".format(sum)
