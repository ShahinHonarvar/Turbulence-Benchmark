
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (gcf) of two numbers at indices 78 and 93 in a list of positive integers
    num1 = my_list[78]
    num2 = my_list[93]
    if num1 > num2:
        smaller_num = num2
        larger_num = num1

    else:

        smaller_num = num1

        larger_num = num2

    # Find the largest prime factor (lp) of the smaller number

    lp = 1

    while smaller_num % lp == 0 and lp < larger_num / 2:

        lp += 1

    if lp * lp > larger_num:

        return smaller_num

    # Find the largest prime factor (lp) of the larger number

    while larger_num % lp == 0 and lp < smaller_num / 2:

        lp += 1

    if lp * lp > smaller_num:

        return smaller_num

    # If no prime factors have been found, the gcf is 1

    else:

        return 1
