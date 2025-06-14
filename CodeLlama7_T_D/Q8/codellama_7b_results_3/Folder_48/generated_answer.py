
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list of integers starting from index 385
    for i in range(385, len(my_list)):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is, append it to the 'even_ints' list
            even_ints.append(my_list[i])
    return even_ints
