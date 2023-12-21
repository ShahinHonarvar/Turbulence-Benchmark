
def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[0]
    b = tuple[-1]
    sum = 0
    binary_str = ""
    hexa_str = ""

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 0 and 8
    for i in range(a + 1, b):
        if i not in tuple:
            sum += i

    # Return the binary or hexadecimal representation string of the sum
    if sum % 2 == 0:
        binary_str = bin(sum)[2:]
        return binary_str

    else:
        hexa_str = hex(sum)
        return hexa_str[2:]
