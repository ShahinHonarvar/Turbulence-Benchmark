
def return_binary_or_hexa(my_tuple):
    # Extract values from tuple
    a = my_tuple[32]
    b = my_tuple[99]
    # Calculate sum of all integers in range that are not present in the tuple
    sum = 0
    for i in range(a + 1, b):
        if i not in my_tuple:
            sum += i
    # Return binary or hexadecimal representation of sum
    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return f"{sum:b}"
