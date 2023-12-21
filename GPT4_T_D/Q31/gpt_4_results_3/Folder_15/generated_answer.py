
def if_perfect_num(num_list):
    index_10_num = num_list[10]
    divisors = [i for i in range(1, index_10_num) if index_10_num % i == 0]
    return sum(divisors) == index_10_num
