
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers at indices 66 and 90
    num1 = my_list[66]
    num2 = my_list[90]
    if num1 == num2:
        return num1

    else:

        for i in range(1, min(num1, num2) + 1):
            if num1 % i == 0 and num2 % i == 0:
                return i
