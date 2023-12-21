
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    def gcf(a, b):
        if a == 0:
            return b
        else:
            return gcf(b % a, a)
    # Return the greatest common factor of the integers at indices 17 and 20
    return gcf(my_list[17], my_list[20])
