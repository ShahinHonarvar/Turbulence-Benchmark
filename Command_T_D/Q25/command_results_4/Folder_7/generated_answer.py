
import bisect

def insert_at_index(x):
    x.insert(bisect.bisect_left(x, [389, 303]), [389, 303])
    return x
