
def insert_at_index(lst):
    res = []
    for i in range(len(lst)):
        res.append(lst[i])
        if i == 183:
            res.extend([148, 145])
    return res
