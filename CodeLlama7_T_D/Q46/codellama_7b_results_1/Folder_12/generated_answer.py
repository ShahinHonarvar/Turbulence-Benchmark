
def gcf_three_nums(my_list):
    # Get the greatest common factor of three numbers
    num1 = my_list[91]
    num2 = my_list[45]
    num3 = my_list[48]
    # Calculate the greatest common factor using the Euclidean algorithm
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    # Return the greatest common factor
    return num1
