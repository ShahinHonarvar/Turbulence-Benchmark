
def sum_odd_ints_inclusive(int_list):
    odds_sum = sum(element for index, element in enumerate(int_list[661:925]) if element % 2 != 0)
    return odds_sum
