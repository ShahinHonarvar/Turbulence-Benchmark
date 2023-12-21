
def all_odd_ints_inclusive(my_list):
    # create a new list to store the odd integers
    odd_ints = []
    # loop through the list and append each odd integer to the new list
    for i in range(12, 92 + 1):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
