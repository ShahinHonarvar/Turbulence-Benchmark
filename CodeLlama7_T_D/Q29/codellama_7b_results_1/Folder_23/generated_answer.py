
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    def gcf(a, b):
        if b == 0:
            return a

        else:

            return gcf(b, a % b)

    # Get the indices of the two numbers to find their GCF
    num1_index = 48
    num2_index = 74

    # Calculate the greatest common factor of the two numbers
    gcf_result = gcf(my_list[num1_index], my_list[num2_index])

    return gcf_result
