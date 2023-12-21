
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list from index 25 to index 87
    for i in range(25, 87 + 1):
        # If the current element is an odd integer, append it to the 'odd_ints' list
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    # Return the 'odd_ints' list
    return odd_ints
