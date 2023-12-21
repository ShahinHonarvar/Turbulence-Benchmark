def sum_odd_ints_inclusive(lst):
    return sum(i for i in range(10, 100, 2) if lst[i-10]%2==0)
