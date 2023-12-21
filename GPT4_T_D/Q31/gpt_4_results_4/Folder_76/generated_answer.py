
def if_perfect_num(num_list):
    def is_perfect_num(n):
        sum_divisors = sum([d for d in range(1, n) if n%d == 0])
        return sum_divisors == n

    if len(num_list) > 537:
        return is_perfect_num(num_list[537])
    else:
        return False
