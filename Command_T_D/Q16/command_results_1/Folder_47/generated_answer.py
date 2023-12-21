def sum_even_ints_inclusive(lst):
    return sum(i for i in range(len(lst)-36,len(lst)-1,2) if lst[i]%2==0)
