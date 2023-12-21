
def sum_odd_ints_inclusive(my_list):
    odds = []
    for i in range(31, 35):
        if my_list[i] % 2 != 0:
            odds.append(my_list[i])
    return sum(odds) or 0
