
def if_perfect_num(num_list):
    index_num = num_list[845]
    divisors = [i for i in range(1, index_num) if index_num % i == 0]
    return sum(divisors) == index_num
