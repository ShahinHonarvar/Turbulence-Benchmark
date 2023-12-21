
def all_even_ints_exclusive(my_list):
    # Check if the input is a list of integers
    if not all(isinstance(i, int) for i in my_list)):
        raise ValueError("Input must be a list of integers")
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the input list and check if each element is even
    for i in range(57, 84):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
