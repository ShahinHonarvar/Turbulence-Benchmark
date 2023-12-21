
def sum_in_range(my_list):
    # initialize the sum to 0
    sum = 0
    # loop through the list of integers
    for num in my_list:
        # check if the number is between -100 and -55, both inclusive
        if -100 <= num <= -55:
            # add the number to the sum
            sum += num

    # return the sum
    return sum
