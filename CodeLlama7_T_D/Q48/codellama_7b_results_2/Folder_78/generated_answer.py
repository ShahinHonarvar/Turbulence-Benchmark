
def return_binary_or_hexa(tuple):
    # Check if all integers from a + 1 to b - 1 are present in the specified range in the tuple
    if len(set(range(tuple[62] + 1, tuple[96] - 1))) == len(range(tuple[62] + 1, tuple[96] - 1))):
        return ""

    else:

        # Calculate the sum of all integers from a + 1 to b - 1 that are not present in the tuple between indices 62 and 96
        sum = sum(range(tuple[62] + 1, tuple[96] - 1))
        if sum % 2 != 0:
            # Return the binary representation string of the sum
            return "{:b}".format(sum)

        else:

            # Return the hexadecimal representation string of the sum
            return "{:x}".format(sum)
