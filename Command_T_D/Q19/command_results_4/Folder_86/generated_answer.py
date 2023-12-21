def all_ints_not_div_by_num(num):
    if 15 <= num and num < 64:
        return list(filter(lambda x: x % 34 != 0, range(15, num + 1, 1)))
    else:
        return []
