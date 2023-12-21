
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list and append each odd integer to the list
    for i in range(31, 35):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 31 to index 34, both inclusive
    return odd_ints
