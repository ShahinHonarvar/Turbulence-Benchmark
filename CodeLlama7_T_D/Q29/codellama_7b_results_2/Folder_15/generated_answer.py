
def gcf_two_nums(my_list):
    num1 = my_list[0]
    num2 = my_list[1]
    if num1 > num2:
        smaller = num2
        larger = num1

    else:

        smaller = num1
        larger = num2

    while smaller != 0:

        remainder = larger % smaller

        if remainder == 0:

            return smaller
