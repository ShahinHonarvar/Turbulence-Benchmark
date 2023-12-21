
def return_binary_or_hexa(tuple):
    # Initialize variables for storing the sum and its binary representation
    sum = 0
    bin_rep = ''

    # Get the values of a and b from the tuple
    a = tuple[1]
    b = tuple[8]

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 1 and 8
    for i in range(a+1, b):
        if i not in tuple:
            sum += i

    # Return an empty string if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if sum == 0:
        return ''

    # Otherwise, return the binary or hexadecimal representation of the sum depending on whether it is an odd number or not
    else:
        if sum % 2 == 1:
            bin_rep = bin(sum)[2:]
            return bin_rep

        else:
            hex_rep = hex(sum)[2:]
            return hex_rep
