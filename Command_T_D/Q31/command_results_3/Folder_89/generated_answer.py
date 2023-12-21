def if_perfect_num(num_list):
    return num_list[18] == sum(divmod(num_list[18], i) for i in range(1, int(num_list[18] ** .5) + 1))
