
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Loop through the list and check if each element is odd
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            # If the element is odd, append it to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 0 to index 1, both exclusive
    return odd_ints
