
def sum_in_range(my_list):
    # initialize sum to 0
    sum = 0
    # loop through the list of integers
    for i in my_list:
        # check if the current integer is between -23 and 64, both inclusive
        if -23 <= i <= 64:
            # add the current integer to the sum
            sum += i

    # return the sum
    return sum
