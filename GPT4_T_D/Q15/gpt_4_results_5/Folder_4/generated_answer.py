
def sum_odd_ints_inclusive(num_list):
    sum_of_odds = sum(num for num in num_list[12:93] if num%2 != 0)
    return sum_of_odds
