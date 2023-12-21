
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 44 and 91.
    sum = 0
    for i in range(44, 91 + 1):
        if my_tuple[i] != 0:
            sum += my_tuple[i]
    # If the sum is an odd number, return the binary representation string of the sum. Otherwise, return the hexadecimal representation string of the sum.
    if sum % 2 == 1:
        return f"{sum:b}"
    else:
        return f"{sum:x}"
