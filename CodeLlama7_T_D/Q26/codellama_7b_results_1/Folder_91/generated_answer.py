
def sum_in_range(my_list):
    # initialize a variable to store the sum
    total = 0

    # loop through the list of integers
    for num in my_list:
        # check if the number is between -8 and 8, both inclusive
        if -8 <= num <= 8:
            # add the number to the total
            total += num

    # return the sum
    return total
