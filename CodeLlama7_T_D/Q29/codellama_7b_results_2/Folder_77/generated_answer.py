
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their greatest common divisor

    num1 = my_list[841]
    num2 = my_list[804]

    if num1 > num2:
        greater_num = num1
        smaller_num = num2

    else:
        greater_num = num2
        smaller_num = num1


    gcf = 1

    while True:

        if greater_num % gcf == 0 and smaller_num % gcf == 0:
            break

        gcf += 1


    return gcf
