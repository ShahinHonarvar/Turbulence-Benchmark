
def return_binary_or_hexa(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 38 and 81
    sum = 0
    for i in range(38, 82):
        if tuple[i] not in range(tuple[37] + 1, tuple[80] - 1):
            sum += tuple[i]
    # If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum
    if sum % 2 == 1:
        return bin(sum).replace("0b", "")
    else:
        return hex(sum).replace("0x", "")
