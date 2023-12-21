
def if_perfect_num(my_list):
    try:
        index = 77
        num = my_list[index]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i

        if sum == num:
            return True

        else:
            return False

    except IndexError:
        return False
