
def sum_odd_ints_inclusive(int_list):
    sum_of_odds = 0
    for i in range(28, 33):
        if i < len(int_list) and int_list[i] % 2 != 0:
            sum_of_odds += int_list[i]
    return sum_of_odds
