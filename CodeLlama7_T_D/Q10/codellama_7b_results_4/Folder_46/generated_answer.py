
def all_odd_ints_exclusive(my_list):
    # Check if the input list is valid
    if not my_list or len(my_list) < 20:
        return []

    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate over the input list and append the odd integers to the output list
    for i in range(20, 43):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    return odd_ints
