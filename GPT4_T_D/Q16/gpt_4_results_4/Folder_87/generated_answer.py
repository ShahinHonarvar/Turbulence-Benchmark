
def sum_even_ints_inclusive(lst):
    start_idx = 36
    end_idx = 46
    even_sum = sum(i for i in lst[start_idx:end_idx+1] if i % 2 == 0)
    return even_sum
