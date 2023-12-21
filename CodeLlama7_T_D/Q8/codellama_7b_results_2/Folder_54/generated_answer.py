
def all_even_ints_exclusive(my_list):
    # Check if the list is empty or None
    if not my_list:
        return []

    # Get the length of the list

    list_length = len(my_list)

    # Initialize an empty list to store the even integers

    even_ints = []

    # Iterate through the list, starting from index 27

    for i in range(27, list_length):

        # Check if the current element is even

        if my_list[i] % 2 == 0:

            # Add the current element to the list of even integers

            even_ints.append(my_list[i])

    return even_ints
