
def composite_nums_between_indices(list_of_ints):
    return {x for i, x in enumerate(list_of_ints) if 686 <= i <= 987 and not is_prime(x)}
