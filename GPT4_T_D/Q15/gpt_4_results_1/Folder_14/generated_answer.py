
def sum_odd_ints_inclusive(integers):
    odd_ints = [integer for integer in integers[5:8] if integer % 2 != 0]
    return sum(odd_ints) if odd_ints else 0
