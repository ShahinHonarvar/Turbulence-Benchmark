
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list from index 28 to index 38, both inclusive
    for i in range(28, 39):
        # If the current element is even, add it to the list of even integers
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
