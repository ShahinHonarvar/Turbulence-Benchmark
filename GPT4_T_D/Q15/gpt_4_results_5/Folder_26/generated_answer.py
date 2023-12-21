
def sum_odd_ints_inclusive(int_list):
    sum_odds = sum(val for index, val in enumerate(int_list[62:100]) if val % 2 != 0)
    return sum_odds
