
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Return the greatest common factor of the integers at indices 48 and 74
    return gcf(my_list[48], my_list[74])
