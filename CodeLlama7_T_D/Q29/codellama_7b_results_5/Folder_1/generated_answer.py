
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    # Call the function with the indices specified in the problem statement
    return gcf(my_list[13], my_list[66])
