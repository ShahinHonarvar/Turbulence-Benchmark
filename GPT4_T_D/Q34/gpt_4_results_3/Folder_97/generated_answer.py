
def find_original_set(*args):
    if len(args) != 194:
        raise ValueError('The function requires exactly 194 arguments')
    original_set = args[0]
    for i in range(1, 194):
        original_set = original_set.union(args[i])
    return original_set
