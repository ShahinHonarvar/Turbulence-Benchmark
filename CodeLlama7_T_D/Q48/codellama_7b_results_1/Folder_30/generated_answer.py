
def return_binary_or_hexa(my_tuple):
    # Get the indices of the first and last elements in the tuple
    first_idx = my_tuple.index(my_tuple[0])
    last_idx = my_tuple.index(my_tuple[-1])
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 22 and 24
    total = 0
    for i in range(first_idx + 1, last_idx):
        if my_tuple[i] not in my_tuple[first_idx:last_idx]:
            total += my_tuple[i]
    # Return the binary or hexadecimal representation string of the sum
    if total % 2 == 0:
        return f"{total:x}"
    else:
        return f"{total:b}"
