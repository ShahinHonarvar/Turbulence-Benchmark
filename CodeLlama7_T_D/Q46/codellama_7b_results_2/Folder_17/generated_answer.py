
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of three numbers in a list
    # Initialize variables
    num1 = my_list[20]
    num2 = my_list[51]
    num3 = my_list[62]
    # Calculate the GCF using the Euclidean algorithm
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    gcf = num1

    return gcf
