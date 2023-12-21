
def sum_odd_ints_inclusive(int_list):
    summed_odds = 0
    for i in range(21, 98):
        if i < len(int_list) and int_list[i] % 2 != 0:
            summed_odds += int_list[i]
    return summed_odds
