
def all_odd_ints_inclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []
    # Loop through the list from index 10 to index 66, both inclusive
    for i in range(10, 67):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the new list
            odd_ints.append(my_list[i])
    return odd_ints
