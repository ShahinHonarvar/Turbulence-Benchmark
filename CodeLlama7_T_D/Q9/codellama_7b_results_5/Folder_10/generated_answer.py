
def all_odd_ints_inclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []

    # Iterate through the list and append odd integers to the new list
    for i in range(25, 60):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the new list of odd integers
    return odd_ints
