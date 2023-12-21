
def return_binary_or_hexa(tuple):
    # Initialize variables for calculating sum
    sum = 0
    # Calculate sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 3 and 9
    for i in range(tuple[3] + 1, tuple[9] - 1):
        if i not in tuple:
            sum += i

    # Check if sum is an odd number
    if sum % 2 == 1:
        return bin(sum)[2:]

    else:
        return hex(sum)[2:]
