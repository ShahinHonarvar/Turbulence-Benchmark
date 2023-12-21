
import itertools

def insert_after_index(lst):
    return [x for x in itertools.chain(lst[:66], [45], lst[66+1:])]
