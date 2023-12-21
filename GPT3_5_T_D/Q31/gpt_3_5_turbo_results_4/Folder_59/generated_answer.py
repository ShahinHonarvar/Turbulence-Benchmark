
def if_perfect_num(lst):
    def is_perfect_num(num):
        divisors_sum = sum([x for x in range(1, num) if num % x == 0])
        return divisors_sum == num

    if len(lst) >= 3:
        return is_perfect_num(lst[2])
    else:
        return False
