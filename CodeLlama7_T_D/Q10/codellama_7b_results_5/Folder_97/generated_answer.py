
def all_odd_ints_exclusive(my_list):
    # Find the index of the first odd integer in the list
    for i in range(20, len(my_list)):
        if my_list[i] % 2 != 0:
            break

    # Create a new list containing all the odd integers from index 20 to index 93, both exclusive
    odd_ints = []

    for i in range(20, 93):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the new list containing all the odd integers from index 20 to index 93, both exclusive
    return odd_ints
