
def composite_nums_between_indices(my_list):
    if len(my_list) < 369:
        return set()
    else:
        return {x for x in my_list[333:368+1] if len(set(range(2, int(x**0.5) + 1))) > 2}
