
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list and check if each element is an odd integer
    for i in range(10, 79):
        if my_list[i] % 2 != 0:
            # If the element is an odd integer, add it to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers in the specified range
    return odd_ints
