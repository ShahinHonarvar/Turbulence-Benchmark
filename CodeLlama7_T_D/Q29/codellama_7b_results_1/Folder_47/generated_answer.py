
def gcf_two_nums(my_list):
    # Get the greatest common factor of two numbers
    def gcf(a, b):
        if a == 0:
            return b
        else:
            return gcf(b % a, a)
    # Call the function with the indices of interest
    return gcf(my_list[28], my_list[17])
