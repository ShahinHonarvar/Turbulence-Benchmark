
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (gcf) of two numbers
    def gcf(a, b):
        if a == 0:
            return b
        else:
            return gcf(b % a, a)
    # Return the gcf of the two specified indices in the list
    return gcf(my_list[66], my_list[90])
