
def sum_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(70, 85):
        if lst[i] % 2 == 1:
            odd_ints.append(lst[i])
    return sum(odd_ints) or 0
