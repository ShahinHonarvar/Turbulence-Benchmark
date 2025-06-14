
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list, starting from index 21
    for i in range(21, len(my_list)):
        # Check if the current element is odd
        if my_list[i] % 2 != 0:
            # If it is odd, add it to the list of odd integers
            odd_ints.append(my_list[i])
    return odd_ints
