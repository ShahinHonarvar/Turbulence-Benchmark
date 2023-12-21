
def if_perfect_num(list_of_pos_int):
    num = list_of_pos_int[28]
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_of_divisors == num
