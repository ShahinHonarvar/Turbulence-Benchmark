
def gcf_two_nums(my_list):
    # find the greatest common factor of two numbers
    # by dividing both numbers by their respective factors until they have no remainder

    num1 = my_list[47]
    num2 = my_list[22]
    if num1 > num2:
        smaller_num = num2
        larger_num = num1

    else:

        smaller_num = num1
        larger_num = num2

    while True:

        if larger_num % smaller_num == 0:
            gcf = smaller_num
            break

        elif smaller_num == 1:
            gcf = 1
            break

        else:

            temp = smaller_num
            smaller_num = larger_num % smaller_num
            larger_num = temp

    return gcf
