
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Return the greatest common factor of the elements at indices 8, 9 and 3
    return gcf(my_list[8], my_list[9]), my_list[3]
