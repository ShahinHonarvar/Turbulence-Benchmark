
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list and append the odd integers to the list
    for i in range(29, 80):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
