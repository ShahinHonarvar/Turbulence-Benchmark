
def sum_odd_ints_inclusive(my_list):
    # initialize sum to 0
    sum = 0
    # loop through list from index 4 to index 8, both inclusive
    for i in range(4, 9):
        # if the current element is odd
        if my_list[i] % 2 != 0:
            # add it to the sum
            sum += my_list[i]
    # return the sum
    return sum
