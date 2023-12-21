
def if_perfect_num(my_list):
    if my_list[828] == sum(filter(lambda x: x % 1 == 0, list(range(my_list[828]))))):
        return True
    else:
        return False
