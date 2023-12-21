
def gcf_two_nums(my_list):
    # Get the greatest common factor of two numbers
    def gcf(a, b):
        if b == 0:
            return a

        else:

            return gcf(b, a % b)

    # Calculate the greatest common factor of the integers at indices 279 and 812
    index_279 = my_list[279]
    index_812 = my_list[812]
    return gcf(index_279, index_812)
