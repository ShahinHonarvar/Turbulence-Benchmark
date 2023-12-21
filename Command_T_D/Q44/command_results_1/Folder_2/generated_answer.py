def composite_nums_between_indices(list):
    res = set()
    for i in range(35, 49):
        res.update(list[i:j] for j in range(i + 1, len(list) + 1, i + 1))
    return res
