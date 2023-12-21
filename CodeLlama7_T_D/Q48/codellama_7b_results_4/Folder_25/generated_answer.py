 def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[37]
    b = tuple[43]
    sum = 0
    binary_rep = ""
    hexa_rep = ""

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 37 and 43
    for i in range(a + 1, b):
        if i not in tuple[37:43]:
            sum += i

    # Return the binary or hexadecimal representation of the sum depending on whether it is an odd number
    if sum % 2 == 1:
        return str(sum)

    else:

        return str(hex(sum))[2:]
