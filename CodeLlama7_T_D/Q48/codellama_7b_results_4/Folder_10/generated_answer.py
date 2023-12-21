
def return_binary_or_hexa(tuple):
    # Get the indices of the tuple
    idx36 = tuple.index(36)
    idx54 = tuple.index(54)
    # Get the integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 36 and 54
    missing_ints = [i for i in range(tuple[idx36] + 1, tuple[idx54] - 1)]
    # Filter out any integers that are present in the specified range in the tuple
    filtered_ints = [i for i in missing_ints if i not in tuple[idx36:idx54]]
    # Calculate the sum of all remaining integers
    sum = sum(filtered_ints)
    # Check if the sum is an odd number
    if sum % 2 == 1:
        # Return the binary representation string of the sum
        return bin(sum)[2:]
    else:
        # Return the hexadecimal representation string of the sum
        return hex(sum)[2:]
