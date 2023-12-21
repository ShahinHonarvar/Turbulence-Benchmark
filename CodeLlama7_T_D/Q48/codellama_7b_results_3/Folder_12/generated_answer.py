
def return_binary_or_hexa(tuple):
    # Get the integers from the tuple
    a = tuple[16]
    b = tuple[87]
    # Calculate the sum of all integers between a + 1 and b - 1 that are not present in the tuple
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple:
            sum += i

    # Return the binary or hexadecimal representation of the sum

    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return f"{sum:b}"
