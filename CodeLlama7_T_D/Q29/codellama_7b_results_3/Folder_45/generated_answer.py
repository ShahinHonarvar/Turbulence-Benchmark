
def gcf_two_nums(my_list):
    # Find the greatest common factor of the two numbers at indices 47 and 97
    num1 = my_list[47]
    num2 = my_list[97]
    if num1 == num2:
        return num1

    else:

        gcf = 1

        for i in range(2, min(num1, num2) + 1):
            if num1 % i == 0 and num2 % i == 0:
                gcf = i

                break

        return gcf
