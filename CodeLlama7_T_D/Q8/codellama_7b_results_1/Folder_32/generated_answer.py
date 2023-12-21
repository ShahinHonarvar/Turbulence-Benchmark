
def all_even_ints_exclusive(my_list):
    # Check if the input is a list of integers
    if not (all([isinstance(x, int) for x in my_list]) and all([x % 2 == 0 for x in my_list])):
        raise ValueError("Input must be a list of even integers.")
    # Get the start and end indices of the specified range
    start = 11
    end = 76
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the input list and append the even integers to the output list
    for i in range(start, end):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
