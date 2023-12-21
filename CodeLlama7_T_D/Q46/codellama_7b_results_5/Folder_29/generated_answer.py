
def gcf_three_nums(my_list):
    # find the greatest common factor of three numbers
    # using the extended euclid algorithm

    def ext_euclid(a, b):
        # compute the greatest common divisor of a and b

        while b != 0:
            t = a % b
            a = b
            b = t

        return a
