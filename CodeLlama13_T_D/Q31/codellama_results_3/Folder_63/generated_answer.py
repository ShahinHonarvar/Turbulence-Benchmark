
def if_perfect_num(my_list):
    n = my_list[57]
    return all(i * i == n for i in range(1, int(n ** 0.5) + 1))
