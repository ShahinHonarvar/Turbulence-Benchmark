
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    num1 = my_list[3]
    num2 = my_list[8]
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
