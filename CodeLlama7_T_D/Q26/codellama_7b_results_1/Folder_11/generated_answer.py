
def sum_in_range(my_list):
    # initialize the sum to 0
    sum = 0
    # loop through the list of integers
    for i in my_list:
        # check if the current integer is between 11 and 76, both inclusive
        if 11 <= i <= 76:
            # if it is, add it to the sum
            sum += i

    # return the sum
    return sum
