
def find_original_set(**kwargs):
    sets = kwargs.values()
    min_set = set(min(sets))
    while True:
        if all(min_set <= s for s in sets):
            return min_set
