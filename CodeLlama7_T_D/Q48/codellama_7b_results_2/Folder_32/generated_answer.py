
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 86 and 90
    a = my_tuple[86]
    b = my_tuple[90]
    sum = 0
    for i in range(a + 1, b):
        if i not in my_tuple:
            sum += i
    # Return the binary or hexadecimal representation string of the sum depending on whether it is an odd number or not
    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return f"{sum:b}"
