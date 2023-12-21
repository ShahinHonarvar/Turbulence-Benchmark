
def sum_ints_div_by_either_nums(my_list):
    # initialize the sum variable to 0
    sum = 0
    
    # loop through the list from index 42 to index 87, both inclusive
    for i in range(42, 88):
        # check if the current element is divisible by -90 or -74
        if my_list[i] % (-90) == 0 or my_list[i] % (-74) == 0:
            # add the current element to the sum variable
            sum += my_list[i]
    
    # return the sum of all integers divisible by either -90 or -74 from index 42 to index 87, both inclusive
    return sum
