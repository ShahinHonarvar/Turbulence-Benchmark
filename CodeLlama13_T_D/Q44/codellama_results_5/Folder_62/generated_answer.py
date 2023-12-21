
def composite_nums_between_indices(my_list):
    return {x for x in my_list[30:87+1] if x > 1 and all(x % y for y in range(2, int(x**0.5) + 1))}
