
def if_perfect_num(num_list):
    if len(num_list) < 163:
        return False
    num = num_list[162]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num
