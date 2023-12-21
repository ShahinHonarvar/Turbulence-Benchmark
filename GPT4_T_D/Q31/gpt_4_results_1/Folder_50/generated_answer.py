
def if_perfect_num(numbers_list):
    if len(numbers_list) > 40:
        num = numbers_list[40]
        sum_ = 0
        for i in range(1, num):
            if num%i == 0:
                sum_ += i
        if sum_ == num:
            return True
    return False
