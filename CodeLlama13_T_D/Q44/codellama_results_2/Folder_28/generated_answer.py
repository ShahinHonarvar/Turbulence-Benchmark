
def composite_nums_between_indices(lst):
    return {i for i in lst[22:89] if len(set(range(1, int(i**0.5)+1)).difference(set(range(int((i-1)**0.5), (i+1)**0.5)))) > 0}
