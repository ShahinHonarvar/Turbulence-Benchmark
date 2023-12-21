
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 55 and 84.
    sum = 0
    for i in range(55, 84 + 1):
        if my_tuple[i] not in range(my_tuple[55], my_tuple[84] + 1)):
            sum += my_tuple[i]
    # If the sum is an odd number, return its binary representation string. Otherwise, return its hexadecimal representation string.
    if sum % 2 == 0:
        return f"0x{sum:X}"
    else:
        return f"0b{sum:b}"
