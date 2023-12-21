
def sum_odd_ints_inclusive(integers):
    odd_integers = [num for num in integers[75:86] if num % 2 != 0]
    return sum(odd_integers) if odd_integers else 0
