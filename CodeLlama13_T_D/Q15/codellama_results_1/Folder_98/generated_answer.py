
def sum_odd_ints_inclusive(my_list):
    odds = []
    for i in range(7):
        if my_list[i] % 2 == 1:
            odds.append(my_list[i])
    return sum(odds)
