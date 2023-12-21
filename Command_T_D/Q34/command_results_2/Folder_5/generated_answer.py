from itertools import chain
def find_original_set(s):
    return {*min(chain(*s), key=len)}
