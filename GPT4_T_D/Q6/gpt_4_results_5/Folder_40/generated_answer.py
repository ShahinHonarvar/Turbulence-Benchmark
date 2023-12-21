
def all_neg_ints_exclusive(lst):
    negatives = [num for i, num in enumerate(lst[1:2]) if num < 0]
    return negatives
