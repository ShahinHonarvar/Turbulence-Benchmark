
def if_perfect_num(lst):
    def is_perfect(num):
        factor_sum = 0
        for i in range(1, num):
            if num%i == 0:
                factor_sum += i
        return factor_sum == num
    try:
        return is_perfect(lst[851])
    except IndexError:
        return False
