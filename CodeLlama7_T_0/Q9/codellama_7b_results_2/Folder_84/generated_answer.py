
def all_odd_ints_inclusive(my_list):
    # Get the length of the list
    list_length = len(my_list)
    # Initialize an empty list to store the odd integers
    odd_integers = []
    # Iterate through the list from index 43 to index 86, both inclusive
    for i in range(43, 87):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_integers.append(my_list[i])
    # Return the list of all odd integers from index 43 to index 86, both inclusive
    return odd_integers
