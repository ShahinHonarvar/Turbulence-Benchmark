
def if_perfect_num(lst):
    if lst[459] == sum([i for i in range(1, lst[459]) if lst[459] % i == 0]):
        return True
    else:
        return False
