
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate over the specified range of indices in the input list
    for i in range(30, 48 + 1):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the output list
            odd_ints.append(my_list[i])
    return odd_ints
