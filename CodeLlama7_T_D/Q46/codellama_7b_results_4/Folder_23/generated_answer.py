
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Calculate the greatest common factor of the elements at indices 31, 25 and 80
    result = gcf(gcf(my_list[31], my_list[25]), my_list[80])
    return result
