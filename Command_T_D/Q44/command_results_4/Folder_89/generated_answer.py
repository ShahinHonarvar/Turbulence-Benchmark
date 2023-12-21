def composite_nums_between_indices(list):
    return {num for num in list[36:46] if all(num % d == 0 for d in range(2, int(num ** .5) + 1)) }
