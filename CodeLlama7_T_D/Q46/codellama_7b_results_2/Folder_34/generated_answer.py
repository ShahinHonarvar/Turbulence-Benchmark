
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Calculate the greatest common factor of the three numbers
    return gcf(my_list[53], my_list[23]), gcf(my_list[45], my_list[23])
