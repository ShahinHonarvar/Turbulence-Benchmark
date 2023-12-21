
def if_perfect_num(num_list):
    def is_perfect_num(num):
        sum_factors = sum(i for i in range(1, int(num / 2) + 1) if num % i == 0)
        return sum_factors == num
    
    return is_perfect_num(num_list[537])
