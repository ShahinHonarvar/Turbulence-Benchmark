
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list, starting from index 11
    for i in range(11, len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    return odd_ints
