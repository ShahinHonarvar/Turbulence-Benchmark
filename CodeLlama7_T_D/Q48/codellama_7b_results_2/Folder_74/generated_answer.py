
def return_binary_or_hexa(tuple):
    # Check if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if all(i in range(tuple[69], tuple[97] + 1)) for i in range(tuple[69] + 1, tuple[97] + 1)):
        # If all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple, return an empty string
        return ""
    else:
        # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 69 and 97
        sum = sum(i for i in range(tuple[69] + 1, tuple[97] + 1) if i not in tuple))
        # Check if the sum is an odd number
        if sum % 2 == 1:
            # If the sum is an odd number, return the binary representation string of the sum
            return bin(sum)[2:]
        else:
            # Otherwise, return the hexadecimal representation string of the sum
            return hex(sum)[2:]
