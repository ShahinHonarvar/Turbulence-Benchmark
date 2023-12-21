
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list and append the odd integers to the 'odd_ints' list
    for i in range(11, 76):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
