
def if_perfect_num(int_list):
    index = 74
    if len(int_list) <= index:
        return False
    num = int_list[index]
    divisor_sum = sum([i for i in range(1, num) if num % i == 0])
    if num == divisor_sum:
       return True
    else:
       return False
