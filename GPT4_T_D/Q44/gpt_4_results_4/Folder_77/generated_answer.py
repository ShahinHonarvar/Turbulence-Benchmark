
def composite_nums_between_indices(lst):
    comp = {i for i in lst[667:775] if i > 1 and any(i % j == 0 for j in range(2, int(i**0.5)+1))}
    return comp
