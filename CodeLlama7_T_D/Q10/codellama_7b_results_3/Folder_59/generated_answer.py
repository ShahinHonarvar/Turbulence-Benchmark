
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list of integers and append each odd integer to the 'odd_ints' list
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 0 to index 9, both exclusive
    return odd_ints
