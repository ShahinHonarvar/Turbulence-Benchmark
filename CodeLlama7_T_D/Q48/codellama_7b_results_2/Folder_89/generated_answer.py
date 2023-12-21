
def return_binary_or_hexa(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 55 and 84
    sum = 0
    for i in range(55, 84 + 1):
        if tuple[i] not in tuple[55:84]:
            sum += tuple[i]
    # If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
