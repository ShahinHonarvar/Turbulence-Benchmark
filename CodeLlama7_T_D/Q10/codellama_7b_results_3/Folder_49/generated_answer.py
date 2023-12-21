
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list, starting from index 80 and ending at index 200 (exclusive)
    for i in range(80, 200):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 80 to index 200 (exclusive)
    return odd_ints
