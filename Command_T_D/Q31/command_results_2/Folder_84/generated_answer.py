def if_perfect_num(list):
    return list[685] == sum(list[0:685]) == sum(list[685+1:])
