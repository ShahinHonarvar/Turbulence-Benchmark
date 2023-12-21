
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 17 and 88.
    sum = 0
    for i in range(17, 88 + 1):
        if my_tuple[i] not in range(my_tuple[17] + 1, my_tuple[88] - 1 + 1):
            sum += my_tuple[i]
    # If the sum is an odd number, return the binary representation string of the sum. Otherwise, return the hexadecimal representation string of the sum.
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
