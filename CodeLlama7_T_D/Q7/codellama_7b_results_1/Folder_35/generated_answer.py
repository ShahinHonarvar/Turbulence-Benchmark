
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers from index 30 to index 48, both inclusive
    for i in range(30, 49):

        # Check if the current element is an even integer

        if my_list[i] % 2 == 0:

            # If it is an even integer, add it to the list of even integers

            even_ints.append(my_list[i])

    # Return the list of all even integers from index 30 to index 48, both inclusive

    return even_ints
