
def if_perfect_num(num_list):
    if len(num_list) < 81:
        return False
    num = num_list[80]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if num == sum:
        return True
    else:
        return False
