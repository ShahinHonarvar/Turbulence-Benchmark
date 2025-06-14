
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (gcf) of two numbers
    def gcf(a, b):
        if b == 0:
            return a

        else:

            return gcf(b, a % b)

    # Return the gcf of the two specified indices in the list
    return gcf(my_list[20], my_list[83])
