
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return gcf(gcf(my_list[96], my_list[57]), my_list[85])
