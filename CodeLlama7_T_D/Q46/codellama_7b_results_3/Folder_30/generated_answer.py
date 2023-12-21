
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers using the Euclidean algorithm
    a = my_list[76]
    b = my_list[35]
    c = my_list[74]
    if a == 0:
        return b

    if b == 0:
        return a

    while True:
        if a > b:
            a, b = b, a

        if a % b == 0:
            return b

        c, d = divmod(a - b, b)

        a, b, c, d = c, d, a, b

    return 1
