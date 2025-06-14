
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate over the list, starting from index 598 (inclusive) and ending at index 767 (exclusive)
    for i in range(598, 767):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers in the specified range, or an empty list if no such integers exist
    return even_ints
