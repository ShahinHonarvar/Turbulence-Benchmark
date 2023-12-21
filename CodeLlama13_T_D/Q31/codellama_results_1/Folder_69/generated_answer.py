
def if_perfect_num(my_list):
    return my_list[459] % 6 == 0 and sum(x for x in my_list[:459] if x < my_list[459]) == my_list[459]
