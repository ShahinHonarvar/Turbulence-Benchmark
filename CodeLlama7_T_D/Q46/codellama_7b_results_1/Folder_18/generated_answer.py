
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of three numbers using Euclid's algorithm
    num1 = my_list[637]
    num2 = my_list[411]
    num3 = my_list[757]
    while num1 != 0:
        num2, remainder = divmod(num2, num1)
        num3, remainder = divmod(num3, num1)
        num1 = remainder

    return num2
