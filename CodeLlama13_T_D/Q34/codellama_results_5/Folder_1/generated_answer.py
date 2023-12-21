
def find_original_set(*args):
    sets = list(args)
    while len(sets) > 0:
        current_set = sets[0]
        for set in sets[1:]:
            if not current_set.issuperset(set):
                return None
