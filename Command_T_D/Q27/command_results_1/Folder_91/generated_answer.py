
def insert_after_index(x):
    return [i for i in x[:2]] + [8] + [i for i in x[3:-1]] + [8] + [x[-1]]
