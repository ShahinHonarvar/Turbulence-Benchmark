
def sum_odd_ints_inclusive(integer_list):
    odd_integers = [i for i in integer_list[56:58] if i % 2 != 0]
    return sum(odd_integers) if odd_integers else 0
