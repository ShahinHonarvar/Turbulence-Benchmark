
def if_perfect_num(num_list):
    num = num_list[43]
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num * 2
