
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list of integers

    for i in range(len(my_list)):

        # Check if the current integer is even and greater than 0

        if my_list[i] % 2 == 0 and my_list[i] > 0:

            # If it is, add it to the list of even integers

            even_ints.append(my_list[i])

    # Return the list of all even integers in the specified range

    return even_ints
