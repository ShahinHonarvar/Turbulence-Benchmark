
def insert_at_index(lst):
    res = lst[:361] + [[699, 556]] + lst[361:-1] + lst[-1:]
    return res
