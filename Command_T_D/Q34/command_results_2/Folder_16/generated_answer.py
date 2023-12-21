from itertools import chain
def find_original_set(s):
    return set(chain(*s))
