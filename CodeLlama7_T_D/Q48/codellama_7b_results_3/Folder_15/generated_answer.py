
def return_binary_or_hexadecimal(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 that are not present in the tuple between indices 0 and 4
    sum = 0
    for i in range(tuple[0] + 1, tuple[4] - 1):
        if i not in tuple:
            sum += i

    # Return the binary or hexadecimal representation of the sum
    if sum % 2 == 0:
        return hex(sum)[2:]

    else:

        return bin(sum)[3:]
