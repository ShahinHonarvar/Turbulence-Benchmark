
def all_odd_ints_exclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []

    # Iterate through the list and append each odd integer to the 'odd_ints' list
    for i in range(86, 100):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the 'odd_ints' list
    return odd_ints
