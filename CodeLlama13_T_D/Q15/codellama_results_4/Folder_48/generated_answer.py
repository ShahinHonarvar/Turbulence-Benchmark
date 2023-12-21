
def sum_odd_ints_inclusive(my_list):
    # initialize result variable to 0
    result = 0
    
    # iterate over list from index 533 to index 605, both inclusive
    for i in range(533, 606):
        # check if current element is odd and add it to the result
        if my_list[i] % 2 != 0:
            result += my_list[i]
    
    # return result
    return result
