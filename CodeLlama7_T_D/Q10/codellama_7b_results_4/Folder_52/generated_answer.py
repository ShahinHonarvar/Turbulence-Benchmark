
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list of integers, starting from index 93 and ending at index 94
    for i in range(93, 95):
        # Check if the current element is odd and add it to the list of odd integers
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
