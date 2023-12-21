
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their
    # least common multiple (LCM) until one number is reached

    num1 = my_list[85]
    num2 = my_list[33]

    if num1 < num2:
        smaller_num = num1
        larger_num = num2

    else:
        smaller_num = num2
        larger_num = num1


    while smaller_num > 0:
        if larger_num % smaller_num == 0:
            lcm = smaller_num
            break

        smaller_num -= 1

    gcf = larger_num // lcm

    return gcf
