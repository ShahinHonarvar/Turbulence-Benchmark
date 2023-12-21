
def all_odd_ints_exclusive(my_list):
    # Check if the input is a list of integers
    if not all(isinstance(x, int) for x in my_list)):
        raise ValueError("The input must be a list of integers")
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate over the list and append the odd integers to the output list
    for i, n in enumerate(my_list):
        if i >= 86 and i < 99 and n % 2 != 0:
            odd_ints.append(n)
    return odd_ints
