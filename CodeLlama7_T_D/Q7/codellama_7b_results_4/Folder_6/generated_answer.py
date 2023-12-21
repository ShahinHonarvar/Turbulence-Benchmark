
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list, starting from index 10 and ending at index 66
    for i in range(10, 67):

        # Check if the current element is an even integer

        if my_list[i] % 2 == 0:

            # If it is, add it to the list of even integers

            even_ints.append(my_list[i])

    # Return the list of all even integers from index 10 to index 66, both inclusive

    return even_ints
