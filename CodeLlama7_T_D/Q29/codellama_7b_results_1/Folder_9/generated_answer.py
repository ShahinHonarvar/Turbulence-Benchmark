
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    # Using the Euclidean Algorithm

    num1 = my_list[84]
    num2 = my_list[63]
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    return num1
