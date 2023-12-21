def all_odd_ints_inclusive(int_list):
    odds = [int(i) for i in int_list if i % 2 == 1]
    return [i for i in odds if i >= 66 and i <= 93]
