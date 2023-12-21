
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # Using the Euclidean algorithm

    a = my_list[19]
    b = my_list[94]

    if a == 0:
        return b
    elif b == 0:
        return a

    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a
