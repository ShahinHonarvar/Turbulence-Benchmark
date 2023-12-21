
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Calculate the greatest common factor of the elements at indices 70, 41 and 20
    return gcf(my_list[70], gcf(my_list[41], my_list[20])))
