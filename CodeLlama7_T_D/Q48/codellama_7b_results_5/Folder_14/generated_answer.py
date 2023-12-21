
def return_binary_or_hexa(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 2 and 5
    sum = 0
    for i in range(2, 6):
        if tuple[i] not in range(tuple[0] + 1, tuple[4] - 1):
            sum += tuple[i]
    # Return the binary representation string of the sum if it is an odd number; otherwise, return the hexadecimal representation string of the sum.
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
