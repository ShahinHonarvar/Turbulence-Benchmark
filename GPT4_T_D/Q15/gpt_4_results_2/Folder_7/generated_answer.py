
def sum_odd_ints_inclusive(integers):
    sum_of_odds = 0
    for index in range(661, 925):
        if index < len(integers) and integers[index] % 2 != 0:
            sum_of_odds += integers[index]
    return sum_of_odds
