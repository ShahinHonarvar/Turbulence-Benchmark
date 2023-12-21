
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Calculate the greatest common factor of the elements at indices 19, 94 and 78
    return gcf(my_list[19], gcf(my_list[94], my_list[78])))
