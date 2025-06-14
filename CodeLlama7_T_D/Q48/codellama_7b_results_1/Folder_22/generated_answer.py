
def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[40]
    b = tuple[200]
    sum = 0

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 40 and 200
    for i in range(a + 1, b):
        if i not in tuple[40:200]:
            sum += i

    # Return the binary or hexadecimal representation string of the sum depending on whether it is an odd number
    if sum % 2 == 0:
        return hex(sum)[2:]

    else:

        return bin(sum)[3:]
