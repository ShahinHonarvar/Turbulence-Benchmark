
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []
    # Iterate through the list from index 50 to index 54, both inclusive
    for i in range(50, 55):
        # If the current element is even, add it to the new list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the new list of even integers
    return even_ints
