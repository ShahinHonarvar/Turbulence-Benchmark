
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list from index 48 to index 74 (both exclusive)
    for i in range(48, 74):
        # If the current element is an odd integer, add it to the 'odd_ints' list
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
