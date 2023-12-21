
def return_binary_or_hexa(tuple):
    # Extract the two integers at indices 68 and 99
    a = tuple[68]
    b = tuple[99]
    # Calculate the sum of all integers from a + 1 to b - 1 that are not present in the specified range in the tuple
    sum = 0
    for i in range(a+1, b):
        if i not in tuple:
            sum += i
    # Return the binary or hexadecimal representation string of the sum depending on whether it is an odd number

    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
