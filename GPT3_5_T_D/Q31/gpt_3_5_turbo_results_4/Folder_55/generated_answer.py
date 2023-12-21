
def if_perfect_num(integer_list):
    return integer_list[21] == sum([i for i in range(1, integer_list[21]) if integer_list[21] % i == 0])
