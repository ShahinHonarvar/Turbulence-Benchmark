
def gcf_two_nums(my_list):
    # find the greatest common factor of two numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # calculate the greatest common factor of the integers at indices 56 and 92
    index_56 = my_list[56]
    index_92 = my_list[92]
    gcf_result = gcf(index_56, index_92)
    return gcf_result
