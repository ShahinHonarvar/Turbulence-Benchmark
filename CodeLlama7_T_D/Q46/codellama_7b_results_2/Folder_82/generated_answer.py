
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of three numbers using the Euclidean algorithm
    def euclid(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    gcf = euclid(my_list[67], my_list[84])
    gcf = euclid(gcf, my_list[13])
    return gcf
