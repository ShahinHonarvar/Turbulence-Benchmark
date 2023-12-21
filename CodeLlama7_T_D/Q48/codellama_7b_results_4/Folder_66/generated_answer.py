
def return_binary_or_hexa(tuple):
    # Extract the integers a and b from the tuple
    a = tuple[11]
    b = tuple[76]
    # Initialize the sum of the integers in the specified range to 0
    sum = 0
    # Iterate through the integers in the specified range, adding them to the sum if they are not present in the tuple between indices 11 and 76
    for i in range(a + 1, b):
        if i not in tuple[11:76]:
            sum += i
    # If the sum is an odd number, return its binary representation string without the prefix '0b'
    if sum % 2 == 1:
        return bin(sum)[2:]
    # Otherwise, return its hexadecimal representation string without the prefix '0x'
    else:
        return hex(sum)[2:]
