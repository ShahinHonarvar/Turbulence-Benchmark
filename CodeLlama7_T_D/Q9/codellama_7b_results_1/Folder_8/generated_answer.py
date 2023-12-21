
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list from index 23 to index 23, both inclusive
    for i in range(23, len(my_list)):
        # Check if the current element is odd
        if my_list[i] % 2 != 0:
            # If it is odd, append it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 23 to index 23, both inclusive
    return odd_ints
