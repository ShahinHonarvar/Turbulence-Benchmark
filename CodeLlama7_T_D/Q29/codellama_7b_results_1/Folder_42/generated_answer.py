
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (GCF) of two numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return gcf(my_list[84], my_list[90])
