
def return_binary_or_hexa(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 that are not present in the tuple between indices 44 and 78
    sum = 0
    for i in range(44, 78):
        if tuple[i] == tuple[i - 1] + 1:
            sum += tuple[i]
    # Return an empty string if all integers from a + 1 to b - 1 are present in the specified range in the tuple
    if sum == 0:
        return ""
    # Otherwise, return the binary or hexadecimal representation of the sum
    elif sum % 2 == 0:
        return f"{sum:#04x}"
    else:
        return f"{sum:#010b}"
