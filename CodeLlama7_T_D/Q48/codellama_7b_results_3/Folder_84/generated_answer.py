
def return_binary_or_hexa(my_tuple):
    # Get the indices of the first and last elements in the tuple
    first_index = my_tuple.index(my_tuple[0])
    last_index = my_tuple.index(my_tuple[-1])
    # Initialize the sum to 0
    sum = 0
    # Iterate over the range of integers between the first and last elements in the tuple
    for i in range(first_index + 1, last_index):
        # Add the current integer to the sum if it is not present in the tuple between indices 32 and 44
        if my_tuple[i] not in my_tuple[32:44]:
            sum += my_tuple[i]
    # If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum.
    if sum % 2 == 1:
        return f"{sum:b}"
    else:
        return f"{sum:x}"
