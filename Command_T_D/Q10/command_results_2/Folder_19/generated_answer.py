def all_odd_ints_exclusive(lst):
    return [n for n in range(2,len(lst)-1,2) if lst[n]%2==1]
