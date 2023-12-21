
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # using the Euclidean algorithm

    a = my_list[49]
    b = my_list[31]

    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a

        return a
