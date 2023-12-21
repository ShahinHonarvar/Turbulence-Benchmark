
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list of integers starting from index 28 and ending at index 40, both inclusive
    for i in range(28, 41):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers found in the specified range, or an empty list if no such integers exist
    return even_ints
