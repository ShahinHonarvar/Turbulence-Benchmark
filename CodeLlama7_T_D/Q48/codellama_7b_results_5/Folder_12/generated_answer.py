
def return_binary_or_hexa(tuple):
    # Check if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if not all(i in tuple for i in range(tuple[16] + 1, tuple[87] - 1)):
        return ""

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 16 and 87
    sum = 0

    for i in range(tuple[16] + 1, tuple[87] - 1):
        if i not in tuple:
            sum += i

    # If the sum is an odd number, return its binary representation string. Otherwise, return its hexadecimal representation string.
    if sum % 2 == 1:
        return bin(sum)[2:]

    else:
        return hex(sum)[2:]
