
def if_perfect_num(my_list):
    if my_list[33] % 6 == 0 and sum(d for d in my_list[:33] if my_list[33] % d == 0) == my_list[33]:
        return True
    else:
        return False
