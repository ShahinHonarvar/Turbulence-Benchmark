
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list from index 66 to index 93, inclusive
    for i in range(66, 94):

        # Check if the current element is even and add it to the list of even integers
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 66 to index 93, both inclusive. If no even integers exist in the specified range, return an empty list.
    return even_ints
