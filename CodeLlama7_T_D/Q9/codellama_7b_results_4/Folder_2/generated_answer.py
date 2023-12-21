
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list and append the odd integers to the 'odd_ints' list
    for i in range(15, 40):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the 'odd_ints' list
    return odd_ints
