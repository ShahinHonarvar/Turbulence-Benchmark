
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 10 and 12
    sum = 0
    for i in range(my_tuple[10] + 1, my_tuple[12]):
        if i not in my_tuple:
            sum += i

    # Return the binary representation string of the sum if it is an odd number; otherwise, return the hexadecimal representation string of the sum.
    if sum % 2 == 1:
        return f'{sum:b}'[2:]
    else:
        return f'{sum:x}'[2:]
