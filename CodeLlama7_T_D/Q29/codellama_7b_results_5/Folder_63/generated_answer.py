
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their
    # common divisors until they have no more divisors in common.

    num1 = my_list[21]
    num2 = my_list[17]
    if num1 > num2:
        smaller_num = num2
        larger_num = num1

    else:

        smaller_num = num1
        larger_num = num2

    while smaller_num != 0:

        remainder = larger_num % smaller_num

        if remainder == 0:

            gcf = smaller_num
            break

        else:

            larger_num = smaller_num
            smaller_num = remainder

    return gcf
