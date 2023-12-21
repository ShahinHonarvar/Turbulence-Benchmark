
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # using the Euclidean algorithm

    a = my_list[4]
    b = my_list[0]
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a
