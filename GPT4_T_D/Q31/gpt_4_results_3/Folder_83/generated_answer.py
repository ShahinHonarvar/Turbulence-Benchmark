
def if_perfect_num(int_list):
    if len(int_list) <= 95:
        return False
    else:
        num = int_list[95]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
