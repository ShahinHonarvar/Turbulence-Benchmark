def find_original_set(s):
    return {*min(set(s), key=lambda x: len(x)),*max(set(s), key=lambda x: len(x)) }
