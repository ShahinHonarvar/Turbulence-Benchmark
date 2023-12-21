
def if_perfect_num(list):
    if len(list) < 27:
        return False
    else:
        if list[27] % (list[27] + sum(list[:27])) == 0:
            return True
        else:
            return False
