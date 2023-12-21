
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the indices of the input list
    for i in range(533, 605 + 1):
        # Check if the current index contains an odd integer
        if my_list[i] % 2 != 0:
            # If it does, add it to the list of odd integers
            odd_ints.append(my_list[i])
    return odd_ints
