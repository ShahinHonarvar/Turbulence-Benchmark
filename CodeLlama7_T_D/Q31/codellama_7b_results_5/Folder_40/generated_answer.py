
def if_perfect_num(my_list):
    if len(my_list) < 8:
        return False

    else:

        num = my_list[7]

        sum = 0

        for i in range(1, int(num ** 0.5)):

            if num % i == 0:

                sum += i + num // i


        if sum - 1 == num:

            return True


        else:

            return False
