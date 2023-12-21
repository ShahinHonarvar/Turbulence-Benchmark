
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Return the greatest common factor of the numbers at indices 23 and 27
    return gcf(my_list[23], my_list[27])
