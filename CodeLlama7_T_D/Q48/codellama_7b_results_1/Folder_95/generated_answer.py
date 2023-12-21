
def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[32]
    b = tuple[99]
    sum = 0

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 32 and 99
    for i in range(a + 1, b):
        if i not in tuple[32:99]:
            sum += i

    # Return the binary or hexadecimal representation string of the sum
    if sum % 2 == 0:
        return f'{sum:x}'
    else:
        return f'{sum:b}'
