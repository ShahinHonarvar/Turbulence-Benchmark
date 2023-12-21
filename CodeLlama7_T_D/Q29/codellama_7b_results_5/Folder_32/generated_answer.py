
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    def gcf(a, b):
        if b == 0:
            return a

        else:

            return gcf(b, a % b)

    # Return the greatest common factor of the integers at indices 47 and 22
    return gcf(my_list[47], my_list[22])
