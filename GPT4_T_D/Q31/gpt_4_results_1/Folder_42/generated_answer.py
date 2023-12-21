
def if_perfect_num(num_list):
    if len(num_list) > 276:
        num = num_list[276]
        sum_of_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_of_divisors += i
        if num == sum_of_divisors:
            return True
    return False
