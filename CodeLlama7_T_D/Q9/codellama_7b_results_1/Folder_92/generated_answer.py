
def all_odd_ints_inclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []

    # Loop through each integer in the list
    for i in range(len(my_list)):
        # Check if the current integer is odd
        if my_list[i] % 2 != 0:
            # If it is, add it to the new list
            odd_ints.append(my_list[i])

    # Return the new list of odd integers
    return odd_ints
