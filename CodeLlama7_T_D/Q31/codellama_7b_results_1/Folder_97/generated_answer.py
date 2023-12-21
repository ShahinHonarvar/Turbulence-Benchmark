
def if_perfect_num(my_list):
    if len(my_list) < 132:
        return False

    else:

        num = my_list[132]

        sum = 0

        for i in range(1, num // 2 + 1):

            if num % i == 0:

                sum += i


        return sum == num
