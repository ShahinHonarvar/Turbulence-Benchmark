
def all_odd_ints_inclusive(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return []

    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list and append odd integers to the list
    for i in range(55, 98 + 1):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    return odd_ints
