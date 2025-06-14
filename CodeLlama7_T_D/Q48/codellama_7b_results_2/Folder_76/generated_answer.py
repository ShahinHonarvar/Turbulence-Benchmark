
def return_binary_or_hexa(tuple):
    # Get the integer stored at index 450 and 905 in the tuple
    a = tuple[450]
    b = tuple[905]
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 450 and 905
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[450:905]:
            sum += i
    # Return the binary or hexadecimal representation string of the sum
    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return f"{sum:b}"
