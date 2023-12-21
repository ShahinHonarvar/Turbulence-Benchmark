
def if_perfect_num(lst):
    def is_perfect(num):
        divisor_sum = sum(i for i in range(1, num) if num % i == 0)
        return divisor_sum == num

    if len(lst) >= 35:
        return is_perfect(lst[34])
    else:
        return False
