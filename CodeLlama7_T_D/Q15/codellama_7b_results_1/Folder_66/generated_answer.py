
def sum_odd_ints_inclusive(my_list):
    # initialize sum to 0
    sum = 0
    # loop through list from index 50 to index 54, both inclusive
    for i in range(50, 55):
        # if the current element is odd, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    # return sum
    return sum
