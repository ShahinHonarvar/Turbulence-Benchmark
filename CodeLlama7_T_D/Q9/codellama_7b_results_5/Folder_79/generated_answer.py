
def all_odd_ints_inclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []
    # Iterate through the list from index 4 to index 4, both inclusive
    for i in range(4, len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the list of odd integers
            odd_ints.append(my_list[i])
    return odd_ints
