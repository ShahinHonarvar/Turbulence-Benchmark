
def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[1]
    b = tuple[7]
    sum = 0
    binary = ''
    hexadecimal = ''

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 1 and 7
    for i in range(a + 1, b):
        if i not in tuple[1:7]:
            sum += i

    # Determine whether the sum is an odd number or not
    if sum % 2 == 0:
        hexadecimal = hex(sum)[2:]

    else:

        binary = bin(sum)[3:]


    # Return the binary representation string of the sum if it is an odd number, otherwise return the hexadecimal representation string of the sum
    if len(binary) > 0:
        return binary

    else:

        return hexadecimal
