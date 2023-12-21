
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers using Euclid's algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Get the elements at the specified indices
    element_1 = my_list[558]
    element_2 = my_list[110]
    element_3 = my_list[628]
    # Find the greatest common factor of these three numbers
    gcf_result = gcf(element_1, gcf(element_2, element_3))
    return gcf_result
