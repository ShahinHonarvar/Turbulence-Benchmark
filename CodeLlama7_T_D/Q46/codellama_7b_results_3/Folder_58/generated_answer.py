
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the three numbers at indices 145, 183 and 770 in the list
    num1 = my_list[145]
    num2 = my_list[183]
    num3 = my_list[770]
    gcf = 1

    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i

            break


    return gcf
