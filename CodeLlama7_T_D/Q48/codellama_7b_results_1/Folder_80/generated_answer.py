
def return_binary_or_hexa(tuple):
    # Extract the integers from the tuple
    a = tuple[57]
    b = tuple[84]
    # Calculate the sum of all integers between a + 1 and b - 1 that are not present in the tuple between indices 57 and 84
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[57:84]:
            sum += i
    # Check if the sum is an odd number
    if sum % 2 == 1:
        return f"{sum:b}"
    else:
        return f"{sum:x}"
