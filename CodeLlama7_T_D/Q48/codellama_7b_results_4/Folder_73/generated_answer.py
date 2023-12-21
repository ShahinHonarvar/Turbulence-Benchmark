
def return_binary_or_hexa(tuple):
    # Get the indices of the integers a and b
    index10 = tuple.index(a)
    index76 = tuple.index(b)
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 10 and 76
    sum = 0
    for i in range(index10 + 1, index76):
        if tuple[i] not in tuple[index10 + 1:index76]:
            sum += tuple[i]
    # Return the binary or hexadecimal representation string of the sum
    if sum % 2 == 0:
        return f"{sum:#0x}"
    else:
        return f"{sum:#0b}"
