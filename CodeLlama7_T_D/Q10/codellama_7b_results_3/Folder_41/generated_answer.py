
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate over the list of integers, starting from index 8 (inclusive) and ending at index 9 (exclusive)
    for i in range(8, len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 8 to index 9 (exclusive)
    return odd_ints
