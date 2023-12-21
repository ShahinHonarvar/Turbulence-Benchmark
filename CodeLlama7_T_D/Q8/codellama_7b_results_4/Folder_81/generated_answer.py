
def all_even_ints_exclusive(my_list):
    # Check if the input is a list of integers
    if not all(isinstance(x, int) for x in my_list)):
        raise ValueError("Input must be a list of integers")
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list and check if each element is even
    for i in range(10, 100):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
