
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # using the Euclidean algorithm

    a = my_list[96]
    b = my_list[32]

    if a == 0:
        return b

    if b == 0:
        return a

    while True:
        r = a % b

        if r == 0:
            return b
