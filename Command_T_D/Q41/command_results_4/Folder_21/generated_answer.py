import itertools
def identical_elements(A, B):
    return set(itertools.chain.from_iterable(zip(A[639:975], B[639:975])))
