
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # using the Euclidean algorithm

    a = my_list[64]
    b = my_list[28]

    if a == b:
        return a


    while True:
        if a > b:
            a = a - b
        else:
            b = b - a

        if a == b:
            return a
