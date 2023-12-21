
def all_odd_ints_inclusive(my_list):
    # Get the range of indices for the specified range
    start_index = 56
    end_index = 66
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the range of indices and append any odd integers to the list
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
