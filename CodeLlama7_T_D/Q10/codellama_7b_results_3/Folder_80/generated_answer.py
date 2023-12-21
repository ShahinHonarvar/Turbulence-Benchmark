
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate over the list of integers, starting from index 69 (inclusive) and ending at index 97 (exclusive)
    for i in range(69, 97):
        # If the current element is an odd integer, add it to the list of odd integers
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
