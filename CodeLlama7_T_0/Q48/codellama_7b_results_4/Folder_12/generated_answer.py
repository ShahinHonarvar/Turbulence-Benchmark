
def return_binary_or_hexa(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 16 and 87
    sum = 0
    for i in range(16, 87):
        if tuple[i] not in range(tuple[16] + 1, tuple[87] - 1)):
            sum += tuple[i]
    # Return the binary or hexadecimal representation string of the sum
    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return f"{sum:b}"
