
def all_odd_ints_exclusive(my_list):
    # Check if the list is empty or None
    if my_list == [] or my_list == None:
        return []

    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list and add odd integers to the new list
    for i in range(27, 34):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    return odd_ints
