
def gcf_two_nums(my_list):
    # find the greatest common factor of two numbers
    # by dividing both numbers by their highest common factor

    # get the indices of the two numbers
    num1 = my_list[20]
    num2 = my_list[83]

    # initialize the greatest common factor to 1
    gcf = 1

    # loop through all factors of both numbers
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            # update the greatest common factor
            gcf = i

    return gcf
