
def all_odd_ints_inclusive(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return []

    # Initialize an empty list to store the odd integers

    odd_integers = []

    # Loop through the list and append the odd integers to the list

    for i in range(12, 92 + 1):
        if my_list[i] % 2 != 0:
            odd_integers.append(my_list[i])

    # Return the list of all odd integers from index 12 to index 92, both inclusive

    return odd_integers
