
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list of integers from index 1 to index 8, both inclusive
    for i in range(1, len(my_list)):

        # Check if the current integer is even

        if my_list[i] % 2 == 0:

            # If it is even, append it to the list of even integers

            even_ints.append(my_list[i])

    # Return the list of all even integers from index 1 to index 8, both inclusive

    return even_ints
