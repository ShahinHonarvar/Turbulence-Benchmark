
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers at indices 3 and 8
    num1 = my_list[3]
    num2 = my_list[8]
    i = 1
    while i <= min(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
