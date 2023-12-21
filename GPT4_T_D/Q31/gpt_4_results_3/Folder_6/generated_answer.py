
def if_perfect_num(int_list):
    try:
        num = int_list[790]
        sum_divisor = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisor += i
        return sum_divisor == num
    except IndexError:
        return False
