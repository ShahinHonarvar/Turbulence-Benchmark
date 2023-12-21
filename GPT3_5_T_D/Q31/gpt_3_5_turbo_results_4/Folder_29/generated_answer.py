
def if_perfect_num(num_list):
    if num_list[19] == sum([i for i in range(1, num_list[19]) if num_list[19] % i == 0]):
        return True
    else:
        return False
