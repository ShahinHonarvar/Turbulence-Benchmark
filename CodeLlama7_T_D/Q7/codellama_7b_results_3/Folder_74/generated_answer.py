
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Loop through the list of integers

    for i in range(17, 78 + 1):

        # Check if the current integer is even

        if my_list[i] % 2 == 0:

            # If it is, add it to the list of even integers

            even_ints.append(my_list[i])

    # Return the list of all even integers from index 17 to index 78, both inclusive

    return even_ints
