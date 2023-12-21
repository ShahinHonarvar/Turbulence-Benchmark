
def if_perfect_num(num_list):
    if len(num_list) > 68:
        num = num_list[68]
        if num > 1:
            sum_divisors = sum([i for i in range(1, num) if num % i == 0])
            if sum_divisors == num:
                return True
    return False
