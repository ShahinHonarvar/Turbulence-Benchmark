
def all_odd_ints_inclusive(my_list):
    # Check if the input is a list of integers
    if not all(isinstance(x, int) for x in my_list)):
        raise ValueError("Input must be a list of integers")
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the input list and append each odd integer to the output list
    for i in range(10, len(my_list)):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    # Return the output list of all odd integers from index 10 to index 10, both inclusive
    return odd_ints
