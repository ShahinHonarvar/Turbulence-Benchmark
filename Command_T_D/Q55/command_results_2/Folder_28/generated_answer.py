def lists_with_product_equal_n(A):
    # n=85, circular list of integers
    # return list of sublists, each of which contains the contiguous integers from the given list
    # such that their product equals 85
    # each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list
    # if no such sublist exists, the function should return an empty list
    # if there are duplicates of such a sublist, they should all be contained in the returned list
    # order of sublists in the returned list does not matter
    #  code does not contain comments
    A.sort()
    A.reverse()
    n = 85
    d = {}
    for i in range(len(A)):
        A[i] = A[i] * i
        d[A[i]] = i
    return [[A[d[a]:d[b]+1] for a in d for b in d if a == b]]
