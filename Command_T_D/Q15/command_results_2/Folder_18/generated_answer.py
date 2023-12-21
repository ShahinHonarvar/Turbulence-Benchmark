def sum_odd_ints_inclusive(lst):
    return sum(i for i in range(35,49+1) if i%2!=0 and i in lst)
