
def gcf_two_nums(my_list):
    # Get the greatest common factor of two numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Return the greatest common factor of the integers at indices 28 and 17
    return gcf(my_list[28], my_list[17])
