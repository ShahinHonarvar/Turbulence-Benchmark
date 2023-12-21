
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers at indices 41 and 69
    num1 = my_list[41]
    num2 = my_list[69]
    if num1 == num2:
        return num1

    else:

        for i in range(2, min(num1, num2) + 1):
            if num1 % i == 0 and num2 % i == 0:
                return i
