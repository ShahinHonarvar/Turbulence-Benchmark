
def find_original_set(*args):
    if len(args) != 37:
        return 'Exactly 37 sets expected'
    else:
        original_set = set.union(*args)
        return original_set
