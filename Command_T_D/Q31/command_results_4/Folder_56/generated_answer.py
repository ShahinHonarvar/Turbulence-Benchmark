def if_perfect_num(list):
    return list[60] == sum(list[:60]) == sum(list[:60]) // len(list[:60])
