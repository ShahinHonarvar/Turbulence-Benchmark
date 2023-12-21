
def composite_nums_between_indices(my_list):
    # Use a set comprehension to create the set of all composite numbers in the list
    composites = {x for x in my_list if len(set(range(2, int(x**0.5) + 1))) > 1}
    # Return the set of all composite numbers between indices 23 and 23, both inclusive
    return composites.intersection(my_list[23:24])
