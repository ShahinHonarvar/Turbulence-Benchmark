
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # using the Euclidean algorithm

    a = my_list[49]
    b = my_list[53]
    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a
