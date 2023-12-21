
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    def gcf(a, b):
        if b == 0:
            return a

        else:

            return gcf(b, a % b)

    # Get the greatest common factor of the two numbers at indices 90 and 84
    return gcf(my_list[90], my_list[84])
