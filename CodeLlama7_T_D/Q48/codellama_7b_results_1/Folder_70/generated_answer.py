
def return_binary_or_hexa(tuple):
    # Initialize variables for the sum and the number of elements in the tuple
    sum = 0
    num_elements = len(tuple)
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 43 and 70
    for i in range(43, 70):
        if tuple[i] is None:
            continue

        else:

            sum += tuple[i]

    # Check if the sum is an odd number

    if sum % 2 == 1:

        return "Binary representation of the sum: " + bin(sum)[2:]

    else:

        return "Hexadecimal representation of the sum: " + hex(sum)[2:]
