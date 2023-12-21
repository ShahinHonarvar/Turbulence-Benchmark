
def sum_odd_ints_inclusive(int_list):
    relevant_ints = int_list[43:87]
    sum_of_odds = sum(i for i in relevant_ints if i % 2 != 0)
    return sum_of_odds
