
def gcf_two_nums(my_list):
    # Find the greatest common factor of two positive integers
    # using the Euclidean algorithm

    a = my_list[85]
    b = my_list[33]

    if a < b:
        a, b = b, a

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a
