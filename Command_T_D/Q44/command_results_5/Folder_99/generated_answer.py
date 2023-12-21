def composite_nums_between_indices(lst):
    lst = set(range(246, 750)) & set(lst)
    return [i for i in lst if i % 2 == 1 and i % 3 == 0]
