
def composite_nums_between_indices(mylist):
    return {x for i, x in enumerate(mylist) if 40 <= i <= 80 and x > 1}
