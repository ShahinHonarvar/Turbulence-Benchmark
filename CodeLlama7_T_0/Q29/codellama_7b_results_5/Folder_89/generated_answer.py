
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their
    # least common multiple until they
    # are equal.

    num1 = my_list[37]
    num2 = my_list[30]

    if num1 > num2:
        smaller_num = num2
        larger_num = num1

    else:
        smaller_num = num1
        larger_num = num2

    while smaller_num != 1:
        if larger_num % smaller_num == 0:
            larger_num //= smaller_num

        else:
            smaller_num -= 1

    return larger_num
