
def gcf_three_nums(my_list):
    # calculate the greatest common factor of the elements at indices 99, 28 and 53
    return gcf(my_list[99], my_list[28], my_list[53])
# helper function to calculate the greatest common factor of two or more numbers
def gcf(a, b):
    while b != 0:
        a, b = b, a % b

    return a
