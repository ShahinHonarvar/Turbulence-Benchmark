
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # using the Euclidean algorithm

    a = my_list[48]
    b = my_list[74]
    if a > b:
        smaller = b
    else:
        smaller = a

    while smaller > 0:

        if a % smaller == 0 and b % smaller == 0:
            gcf = smaller
            break

        smaller -= 1

    return gcf
