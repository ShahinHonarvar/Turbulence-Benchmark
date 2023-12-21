
def all_odd_ints_inclusive(my_list):
    # initialize an empty list to store the odd integers
    odd_ints = []
    # loop through the list of integers, starting at index 15 and ending at index 39, inclusive
    for i in range(15, 40):
        # if the current element is an odd integer, add it to the list of odd integers
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
