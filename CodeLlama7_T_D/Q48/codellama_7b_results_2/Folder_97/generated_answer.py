
def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[34]
    b = tuple[69]
    sum = 0

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 34 and 69
    for i in range(a + 1, b):
        if i not in tuple[34:69]:
            sum += i

    # If the sum is an odd number, return the binary representation string of the sum; otherwise, it should return the hexadecimal representation string of the sum.
    if sum % 2 == 1:
        return "binary" + bin(sum)[2:]

    else:

        return "hexadecimal" + hex(sum)[2:]
