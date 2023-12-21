 def return_binary_or_hexa(tuple):
    # Initialize variables
    sum = 0
    binary_string = ""
    hexadecimal_string = ""

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 36 and 52
    for i in range(tuple[36], tuple[52] + 1):
        if i not in tuple:
            sum += i

    # Determine whether the sum is an odd number
    if sum % 2 == 0:
        hexadecimal_string = hex(sum)[2:]

    else:

        binary_string = bin(sum)[3:]

        # Return an empty string if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
        if len(tuple[36:52]) == sum - tuple[36] - tuple[52]:
            return ""

    # Return the binary or hexadecimal representation string of the sum
    if binary_string != "":

        return "0b" + binary_string

    else:

        return "0x" + hexadecimal_string
