
def return_binary_or_hexa(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 10 and 28
    a = tuple[10]
    b = tuple[28]
    sum = 0

    for i in range(a + 1, b):
        if i not in tuple:
            sum += i

    # Return the binary or hexadecimal representation string of the sum depending on whether it is an odd number or not
    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return f"{sum:b}"
