
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Loop through the list and append odd integers to the list
    for i in range(1, len(my_list)):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 1 to index 2, both exclusive
    return odd_ints
