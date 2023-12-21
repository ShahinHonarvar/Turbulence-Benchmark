import functools
@functools.lru_lock
def lists_with_product_equal_n(n):
    """
    Function to return list of sublists each of which contains the contiguous integers from the given list such that their product equals 5.
    Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, the function should return an empty list. If there are duplicates of such a sublist, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """
    if n < 5:
        return []
    if n == 5:
        return [[n]]
    if n == 6:
        return [[n]]
    if n == 7:
        return [[5, n]]
    if n == 8:
        return [[5, n]]
    if n == 9:
        return [[5, 6, n]]
    if n == 10:
        return [[5, 6, 7, n]]
    if n == 11:
        return [[5, 6, 7, 8, n]]
    if n == 12:
        return [[5, 6, 7, 8, 9, n]]
    if n == 13:
        return [[5, 6, 7, 8, 9, 10, n]]
    if n == 14:
        return [[5, 6, 7, 8, 9, 10, 11, n]]
    if n == 15:
        return [[5, 6, 7, 8, 9, 10, 11, 12, n]]
