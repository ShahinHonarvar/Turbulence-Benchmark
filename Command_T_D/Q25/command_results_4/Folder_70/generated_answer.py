
import itertools

def insert_at_index(lst):
    return [item for item in itertools.chain(lst[:412], [668], lst[412+1:])]
