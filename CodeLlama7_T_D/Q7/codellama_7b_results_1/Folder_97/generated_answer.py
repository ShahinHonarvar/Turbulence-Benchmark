
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list from index 40 to index 80, both inclusive
    for i in range(40, 81):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 40 to index 80, both inclusive
    return even_ints
