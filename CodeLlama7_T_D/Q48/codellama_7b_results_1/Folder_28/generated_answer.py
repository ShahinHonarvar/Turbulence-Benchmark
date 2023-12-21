
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 86 and 99
    my_sum = 0
    for i in range(87, 100):
        if my_tuple[i] not in range(my_tuple[86] + 1, my_tuple[99] - 1):
            my_sum += my_tuple[i]
    # Return the binary representation string of the sum if it is an odd number; otherwise, return the hexadecimal representation string of the sum.
    if my_sum % 2 == 0:
        return f"{my_sum:x}"
    else:
        return f"{my_sum:b}"
