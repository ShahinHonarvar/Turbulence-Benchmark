
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Return the greatest common factor of the elements at indices 59, 93 and 84
    return gcf(my_list[59], my_list[93]) * gcf(my_list[59], my_list[84]) * gcf(my_list[93], my_list[84])
