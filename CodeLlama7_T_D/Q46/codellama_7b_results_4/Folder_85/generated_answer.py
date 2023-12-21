
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (gcf) of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Extract the desired elements from the list
    num1 = my_list[49]
    num2 = my_list[46]
    num3 = my_list[13]
    # Calculate the gcf of these numbers
    gcf_result = gcf(num1, gcf(num2, num3))
    return gcf_result
