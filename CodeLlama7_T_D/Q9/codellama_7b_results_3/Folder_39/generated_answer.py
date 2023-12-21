
def all_odd_ints_inclusive(my_list):
    # create a new list to store the odd integers
    odd_ints = []
    # loop through the list of integers, starting from index 20
    for i in range(20, len(my_list)):
        # check if the current integer is odd
        if my_list[i] % 2 != 0:
            # if it is odd, add it to the new list of odd integers
            odd_ints.append(my_list[i])
    # return the list of all odd integers from index 20 to index 30, both inclusive
    return odd_ints
