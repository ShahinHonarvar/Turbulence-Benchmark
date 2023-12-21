
def sum_odd_ints_inclusive(my_list):
    # initialize sum to 0
    sum = 0
    # loop through list starting from index 661
    for i in range(661, len(my_list)):
        # check if current element is odd
        if my_list[i] % 2 != 0:
            # add current element to sum
            sum += my_list[i]
    return sum
