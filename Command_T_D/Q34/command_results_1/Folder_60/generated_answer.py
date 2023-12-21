def find_original_set(x):
    return {i for i in range(1,len(x)+1) if all(x[i].issubset(y) for y in x)}
