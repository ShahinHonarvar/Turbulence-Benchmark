
def all_odd_ints_inclusive(my_list):
    # create a new list to store the odd integers
    odd_ints = []
    # loop through the list of integers, starting at index 70 and ending at index 200 (both inclusive)
    for i in range(70, 201):
        # check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # if it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # return the list of all odd integers from index 70 to index 200 (both inclusive), or an empty list if no odd integers exist in the specified range
    return odd_ints
