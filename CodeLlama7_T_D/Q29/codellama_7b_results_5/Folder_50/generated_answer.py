
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (GCF) of the two numbers
    number1 = my_list[90]
    number2 = my_list[54]
    while number2 != 0:
        remainder = number1 % number2
        number1 = number2
        number2 = remainder

    return number1
