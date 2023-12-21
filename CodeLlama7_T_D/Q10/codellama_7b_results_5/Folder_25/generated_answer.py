
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list of integers, starting from index 41 and ending at index 69 (both exclusive)
    for i in range(41, 70):
        # If the current element is an odd integer, add it to the list of odd integers
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 41 to index 69 (both exclusive)
    return odd_ints
