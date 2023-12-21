
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by iteratively dividing the larger number
    # by the smaller number until the result is 1

    num1 = my_list[88]
    num2 = my_list[35]

    if num1 > num2:
        smaller_num = num2
        larger_num = num1

    else:
        smaller_num = num1
        larger_num = num2

    while smaller_num != 0:
        temp = larger_num % smaller_num
        larger_num = smaller_num
        smaller_num = temp

    return larger_num
