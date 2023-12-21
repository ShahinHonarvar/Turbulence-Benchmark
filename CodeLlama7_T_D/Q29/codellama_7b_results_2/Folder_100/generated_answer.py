
def gcf_two_nums(my_list):
    # Get the greatest common factor of two numbers
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Return the greatest common factor of the specified indices in the list
    return gcf(my_list[96], my_list[32])
