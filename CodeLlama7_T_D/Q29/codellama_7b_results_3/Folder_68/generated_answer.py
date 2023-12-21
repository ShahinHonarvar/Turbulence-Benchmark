
def gcf_two_nums(my_list):
    # find the greatest common factor of two numbers
    # using the Euclidean algorithm

    a = my_list[8]
    b = my_list[9]
    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a
