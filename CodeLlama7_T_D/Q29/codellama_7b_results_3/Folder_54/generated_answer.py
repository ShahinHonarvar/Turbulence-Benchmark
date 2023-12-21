 def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by iteratively dividing the smaller number
    # by the larger number and checking if
    # the result is equal to 1

    num1 = my_list[56]

    num2 = my_list[92]

    if num1 > num2:
        smaller_num = num2
        larger_num = num1

    else:
        smaller_num = num1
        larger_num = num2

    while smaller_num != 0 and larger_num % smaller_num != 0:
        smaller_num -= 1

    return smaller_num
