
def sum_odd_ints_inclusive(lst):
    sum_of_odds = sum(num for num in lst[1:9] if num % 2 != 0)
    return sum_of_odds if sum_of_odds else 0
