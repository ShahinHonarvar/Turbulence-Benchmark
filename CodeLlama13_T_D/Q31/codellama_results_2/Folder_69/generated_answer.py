
def if_perfect_num(my_list):
    if my_list[459] == sum(filter(lambda x: my_list[459] % x == 0, range(1, int(my_list[459]) // 2 + 1)))
        return True
    else:
        return False
