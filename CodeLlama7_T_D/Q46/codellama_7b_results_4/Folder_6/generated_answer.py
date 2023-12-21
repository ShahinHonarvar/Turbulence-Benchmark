
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 93, 94 and 57
    # Define a function to calculate the greatest common factor of two numbers
    def gcf(a, b):
        while (b != 0):
            a, b = b, a % b
        return a

    # Call the function to calculate the greatest common factor of the elements at indices 93, 94 and 57
    return gcf(gcf(my_list[93], my_list[94]), my_list[57])
