 def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list from index 69 to index 97, exclusive
    for i in range(69, 97):
        # If the current element is even, append it to the list of even integers
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
