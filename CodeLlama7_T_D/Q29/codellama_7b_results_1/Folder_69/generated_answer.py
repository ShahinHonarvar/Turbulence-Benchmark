
def gcf_two_nums(my_list):
    # find the greatest common factor of two numbers
    # using the Euclidean algorithm

    a = my_list[894]
    b = my_list[801]

    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a
