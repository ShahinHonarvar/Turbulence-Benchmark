
def return_binary_or_hexa(tuple):
    # Get the indices of a and b in the tuple
    i = 7
    j = 9

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 7 and 9
    sum = 0
    for k in range(tuple[i] + 1, tuple[j]):
        if k not in tuple:
            sum += k

    # Return an empty string if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if sum == 0:
        return ""

    # Otherwise, return the binary or hexadecimal representation string of the sum
    elif sum % 2 == 0:
        return f"{sum:x}"
    else:
        return f"{sum:b}"
