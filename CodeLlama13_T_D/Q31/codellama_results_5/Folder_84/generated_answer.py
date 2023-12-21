
def if_perfect_num(my_list):
    return my_list[685] in [x for x in range(1, int(math.sqrt(my_list[685])) + 1) if my_list[685] % x == 0]
