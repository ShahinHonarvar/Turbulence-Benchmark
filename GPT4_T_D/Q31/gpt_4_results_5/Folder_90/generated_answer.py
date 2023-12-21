
def if_perfect_num(num_list):
    try:
        number = num_list[263]
        sum_num = 0
        for i in range(1, number):
            if number % i == 0:
                sum_num += i
        if sum_num == number:
            return True
        else:
            return False
    except IndexError:
        return False
