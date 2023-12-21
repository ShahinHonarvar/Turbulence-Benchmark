
def sum_odd_ints_inclusive(lst):
    odd_ints = [num for num in lst[62:64] if num % 2 != 0]
    return sum(odd_ints) if len(odd_ints) > 0 else 0
