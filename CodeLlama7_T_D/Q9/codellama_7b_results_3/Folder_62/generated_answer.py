
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list and append the odd integers to the empty list
    for i in range(91, 100):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 91 to index 99, both inclusive
    return odd_ints
