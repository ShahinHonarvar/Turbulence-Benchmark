
def sum_odd_ints_inclusive(my_list):
    # initialize sum to 0
    sum = 0
    # loop through list from index 55 to index 98, both inclusive
    for i in range(55, 100):
        # if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # add the current element to the sum
            sum += my_list[i]
    # return the sum
    return sum
