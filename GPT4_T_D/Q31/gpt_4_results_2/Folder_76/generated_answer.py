
def if_perfect_num(num_list):
    if len(num_list) > 537:
        num = num_list[537]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
    return False
