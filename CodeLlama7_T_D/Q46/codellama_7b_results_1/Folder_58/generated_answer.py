
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Return the greatest common factor of the elements at indices 145, 183 and 770
    return gcf(gcf(my_list[145], my_list[183]), my_list[770])
