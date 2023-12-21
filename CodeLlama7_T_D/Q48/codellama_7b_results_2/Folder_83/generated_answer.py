
def return_binary_or_hexa(tuple):
    # Extract the integers from the tuple
    a = tuple[90]
    b = tuple[200]
    # Calculate the sum of all integers between a + 1 and b - 1 that are not present in the tuple
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple:
            sum += i

    # Return the binary or hexadecimal representation of the sum depending on whether it is an odd number

    if sum % 2 == 1:
        return f"{sum:#b}"

    else:
        return f"{sum:#x}"
