
def all_odd_ints_inclusive(my_list):
    # Find the starting and ending indices of the range
    start_index = 29
    end_index = 79
    # Create an empty list to store the odd integers
    odd_integers = []
    # Iterate through the list and append the odd integers to the empty list
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            odd_integers.append(my_list[i])
    # Return the list of all odd integers from index 29 to index 79, both inclusive
    return odd_integers
