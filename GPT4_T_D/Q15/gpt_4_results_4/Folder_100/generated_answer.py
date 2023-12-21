
def sum_odd_ints_inclusive(int_list):
    summed_odds = sum(i for i in int_list[42:69] if i % 2 != 0)
    return summed_odds
