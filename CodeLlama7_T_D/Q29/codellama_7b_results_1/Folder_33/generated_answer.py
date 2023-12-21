
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # using the Euclidean algorithm

    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return gcf(my_list[166], my_list[106])
