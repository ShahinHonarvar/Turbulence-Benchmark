def sum_in_range(x):
    return sum(x[i] for i in range(len(x)) if 10 <= x[i] <= 97)
