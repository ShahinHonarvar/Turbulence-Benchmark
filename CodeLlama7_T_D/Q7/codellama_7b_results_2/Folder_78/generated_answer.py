
def all_even_ints_inclusive(my_list):
    # Define a new list to store the even integers
    even_ints = []
    # Loop through the list of integers starting at index 43
    for i in range(43, len(my_list)):
        # Check if the current integer is even and add it to the new list if it is
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
