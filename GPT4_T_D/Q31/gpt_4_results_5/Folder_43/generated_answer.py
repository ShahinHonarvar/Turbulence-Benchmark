
def if_perfect_num(int_list):
    index = 29
    if index < len(int_list):
        num = int_list[index]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
    return False
