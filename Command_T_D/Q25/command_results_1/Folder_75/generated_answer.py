
def insert_at_index(x):
    return [i for i in x[:99]] + [99] + [i for i in x[99:-1]] + [99] + [i for i in x[99:-1]]
