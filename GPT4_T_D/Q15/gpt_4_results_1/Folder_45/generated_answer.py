
def sum_odd_ints_inclusive(lst):
    if len(lst) < 201:
        upper_limit = len(lst)
    else:
        upper_limit = 201

    sum_odd_ints = 0
    for i in range(30, upper_limit):
        if lst[i] % 2 != 0:
            sum_odd_ints += lst[i]

    return sum_odd_ints
