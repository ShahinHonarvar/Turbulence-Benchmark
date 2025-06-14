
def all_odd_ints_inclusive(my_list):
    # Get the range of indices for the specified list
    start_index = 26
    end_index = 52
    # Initialize an empty list to store the odd integers
    odd_integers = []
    # Iterate through the range of indices and check if each element is an odd integer
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            # If the element is an odd integer, append it to the list of odd integers
            odd_integers.append(my_list[i])
    return odd_integers
