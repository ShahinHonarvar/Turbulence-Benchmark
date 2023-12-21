
def all_even_ints_inclusive(my_list):
    # Create a slice of the list from index 75 to index 88, both inclusive
    even_ints = my_list[75:89]
    # Initialize an empty list to store the even integers
    even_int_list = []
    # Iterate over the elements in the slice and append them to the empty list if they are even
    for i in even_ints:
        if i % 2 == 0:
            even_int_list.append(i)
    # Return the list of even integers
    return even_int_list
