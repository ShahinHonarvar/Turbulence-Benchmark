def sum_in_range(a):
    return sum(a[i] for i in range(len(a)) if 18 <= a[i] <= 60)
