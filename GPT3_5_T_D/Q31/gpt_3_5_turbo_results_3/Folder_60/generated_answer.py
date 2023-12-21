
def if_perfect_num(num_list):
    def is_perfect(num):
        factor_sum = 0
        for i in range(1, num):
            if num % i == 0:
                factor_sum += i
        return factor_sum == num

    if len(num_list) > 88 and is_perfect(num_list[88]):
        return True
    else:
        return False
