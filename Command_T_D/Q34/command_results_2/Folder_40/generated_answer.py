def find_original_set(s):
    return {i for i in range(min(s), max(s) + 1) if all(i in x for x in s)}
