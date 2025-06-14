
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list of integers from index 8 to index 9, both inclusive
    for i in range(8, 10):
        # If the current integer is even, add it to the list of even integers
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
