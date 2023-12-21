
def all_odd_ints_inclusive(my_list):
    # Check if the input is a list of integers
    if not all(isinstance(x, int) for x in my_list)):
        raise ValueError("Input must be a list of integers")
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the input list and append any odd integers to the output list
    for i in range(30, 87 + 1):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
