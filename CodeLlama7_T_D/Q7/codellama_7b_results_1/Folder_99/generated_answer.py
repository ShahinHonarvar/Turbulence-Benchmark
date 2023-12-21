
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list from index 310 to index 370 (both inclusive)
    for i in range(310, 371):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the list of even integers
            even_ints.append(my_list[i])
    return even_ints
