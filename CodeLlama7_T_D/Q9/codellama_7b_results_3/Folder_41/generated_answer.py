
def all_odd_ints_inclusive(my_list):
    # Check if the input is a list of integers
    if not (isinstance(my_list, list) and all(isinstance(i, int) for i in my_list)):
        raise ValueError("Input must be a list of integers")
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate over the input list
    for i in range(len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 6 to index 6, both inclusive
    return odd_ints
