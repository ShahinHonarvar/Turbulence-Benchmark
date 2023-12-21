 def all_even_ints_inclusive(my_list):
    # Initialize a new list to store the even integers
    even_ints = []
    # Iterate through the specified range of indices in the input list
    for i in range(73, len(my_list)):
        # If the current element is an even integer, append it to the 'even_ints' list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
