
def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[20]
    b = tuple[51]
    sum = 0
    binary = ''
    hexa = ''

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 20 and 51
    for i in range(a + 1, b):
        if i not in tuple[20:51]:
            sum += i

    # Convert the sum to binary or hexadecimal representation string
    if sum % 2 == 0:
        binary = bin(sum)[2:]

    else:
        hexa = hex(sum)[2:]

    # Return the appropriate representation string based on whether the sum is an odd number or not
    if len(hexa) > len(binary):
        return hexa

    else:
        return binary
