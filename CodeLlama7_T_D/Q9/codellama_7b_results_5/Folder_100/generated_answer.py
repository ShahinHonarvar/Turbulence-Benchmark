
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list and append the odd integers to the 'odd_ints' list
    for i in range(42, 68 + 1):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 42 to index 68, both inclusive
    return odd_ints
