
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers
    # using the Euclidean algorithm

    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    a = my_list[37]
    b = my_list[30]
    c = my_list[48]
    gcf_abc = gcf(gcf(a, b), c)
    return gcf_abc
