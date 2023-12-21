
def return_binary_or_hexa(tuple):
    # Extract the elements between indices 86 and 89
    a = tuple[86]
    b = tuple[89]
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 86 and 89
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[86:89]:
            sum += i
    # Return the binary or hexadecimal representation string of the sum
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
