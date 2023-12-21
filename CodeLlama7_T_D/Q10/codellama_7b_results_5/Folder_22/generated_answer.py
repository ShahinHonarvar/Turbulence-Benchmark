
def all_odd_ints_exclusive(my_list):
    # create a new list to store the odd integers
    odd_ints = []
    # loop through the list of integers, starting at index 40 and ending at index 200 (exclusive)
    for i in range(40, 200):
        # if the current element is an odd integer, add it to the new list
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
