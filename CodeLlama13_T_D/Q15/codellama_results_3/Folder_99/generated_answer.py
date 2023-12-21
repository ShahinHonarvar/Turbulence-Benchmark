
def sum_odd_ints_inclusive(my_list):
    odds = []
    for i in range(310, 371):
        if my_list[i] % 2 == 1:
            odds.append(my_list[i])
    return sum(odds)
