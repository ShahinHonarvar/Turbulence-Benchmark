
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    def gcf(a, b):
        if b == 0:
            return a

        else:

            return gcf(b, a % b)

    # Return the greatest common factor of the two numbers at indices 0 and 9
    return gcf(my_list[0], my_list[9])
