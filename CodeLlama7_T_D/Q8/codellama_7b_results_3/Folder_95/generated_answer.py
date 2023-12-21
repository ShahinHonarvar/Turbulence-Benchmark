
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list from index 25 to 80, both exclusive
    for i in range(25, 80):
        # Check if the current element is even and not already in the 'even_ints' list
        if my_list[i] % 2 == 0 and my_list[i] not in even_ints:
            # If it is even and not already in the list, add it to the 'even_ints' list
            even_ints.append(my_list[i])
    return even_ints
