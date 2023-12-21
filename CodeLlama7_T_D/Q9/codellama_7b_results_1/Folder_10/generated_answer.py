
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list from index 25 to 59, both inclusive
    for i in range(25, 60):
        # If the current element is an odd integer, append it to the list of odd integers
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
