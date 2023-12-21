
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers using Euclid's algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Find the greatest common factor of the elements at indices 15, 51 and 76
    idx1 = 15
    idx2 = 51
    idx3 = 76

    gcf_val = gcf(gcf(my_list[idx1], my_list[idx2]), my_list[idx3])
    return gcf_val
