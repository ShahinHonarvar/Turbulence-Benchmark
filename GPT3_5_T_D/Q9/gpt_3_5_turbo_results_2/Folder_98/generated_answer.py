
def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(7):  # iterate from index 0 to index 6
        if i < len(lst) and lst[i] % 2 != 0:  # check if the current number is odd
            odd_ints.append(lst[i])  # if yes, add it to the list
    return odd_ints  # return the list of odd integers
