
def gcf_three_nums(my_list):
    # calculate the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # get the indices of the three numbers to find the GCF of
    indices = [990, 671, 711]
    # get the values of the three numbers at the specified indices
    values = [my_list[i] for i in indices]
    # calculate the GCF of the three numbers
    gcf_val = gcf(values[0], values[1])
    return gcf_val
