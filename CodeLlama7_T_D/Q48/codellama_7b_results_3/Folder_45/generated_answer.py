
def return_binary_or_hexa(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 30 and 200
    sum = 0
    for i in range(30, 200):
        if tuple[i] == tuple[i-1] + 1:
            sum += tuple[i-1] + 1
    # If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum.
    if sum % 2 == 0:
        return f"{sum:#x}"
    else:
        return f"{sum:#b}"
