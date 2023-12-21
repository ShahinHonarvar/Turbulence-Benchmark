
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list of integers from index 60 to index 200, both inclusive
    for i in range(60, 201):
        # If the current integer is even, append it to the list of even integers
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
