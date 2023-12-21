
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the specified range of indices in my_list
    for i in range(66, 94):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers in the specified range, or an empty list if no such integers exist
    return even_ints
