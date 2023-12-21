
def all_odd_ints_inclusive(my_list):
    # Define start and end indices for the range of odd integers
    start_index = 59
    end_index = 97
    # Initialize an empty list to store the odd integers
    odd_integers = []
    # Iterate through the list from start_index to end_index
    for i in range(start_index, end_index + 1):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_integers.append(my_list[i])
    # Return the list of all odd integers from index 59 to index 97, both inclusive
    return odd_integers
