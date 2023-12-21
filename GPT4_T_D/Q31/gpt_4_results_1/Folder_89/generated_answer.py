
def if_perfect_num(num_list):
    if len(num_list) > 18:
        num = num_list[18]
        sum_divisors = sum(i for i in range(1, num) if num % i == 0)
        if sum_divisors == num:
            return True
    return False
