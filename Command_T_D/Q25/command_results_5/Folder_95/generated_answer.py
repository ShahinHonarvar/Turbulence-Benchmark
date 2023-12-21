
import itertools

def insert_at_index(lst):
    # Create a list of tuples of indices where the element should be inserted
    insert_idxs = [(i, i) for i in range(len(lst) + 1)]
    # Insert the element at all the indices
    lst = list(itertools.zip_longest(lst, [80] * len(lst), fillvalue=0))
    # Filter out the elements that were not inserted
    return [x for x, _ in filter(lambda _, y: y, lst)]
