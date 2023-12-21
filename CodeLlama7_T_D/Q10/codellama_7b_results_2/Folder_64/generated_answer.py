
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate over the list of integers and check if each element is odd
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            # If the current element is odd, add it to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 0 to index 4, both exclusive
    return odd_ints
