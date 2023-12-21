
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers using Euclid's algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return gcf(gcf(my_list[412], my_list[932]), my_list[337]))
