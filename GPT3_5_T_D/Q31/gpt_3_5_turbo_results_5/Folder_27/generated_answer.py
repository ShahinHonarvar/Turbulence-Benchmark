
def if_perfect_num(num_list):
    def is_perfect_num(num):
        sum_factors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_factors += i
        return sum_factors == num

    return is_perfect_num(num_list[56])
