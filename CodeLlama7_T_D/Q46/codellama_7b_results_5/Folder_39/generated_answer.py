
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Get the indices of the three numbers
    ind1 = 85
    ind2 = 36
    ind3 = 54

    # Find the greatest common factor of these three numbers
    gcf_val = gcf(my_list[ind1], gcf(my_list[ind2], my_list[ind3])))

    return gcf_val
