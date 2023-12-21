
def all_odd_ints_exclusive(my_list):
    # Check if the list is empty or if the range is invalid
    if len(my_list) == 0 or my_list[50:92] == []:
        return []

    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list and append each odd integer to the 'odd_ints' list
    for i in range(50, 92):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 50 to index 92, both exclusive
    return odd_ints
