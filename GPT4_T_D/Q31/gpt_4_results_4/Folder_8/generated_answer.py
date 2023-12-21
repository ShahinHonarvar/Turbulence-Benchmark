
def if_perfect_num(num_list):
    num = num_list[49]
    factors = [i for i in range(1, num) if num % i == 0]
    return sum(factors) == num
