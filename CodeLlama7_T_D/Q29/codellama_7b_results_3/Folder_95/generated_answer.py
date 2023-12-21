
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # using the Euclidean algorithm

    a = my_list[43]
    b = my_list[99]
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        while b != 0:
            remainder = a % b
            a = b
            b = remainder

        return a
