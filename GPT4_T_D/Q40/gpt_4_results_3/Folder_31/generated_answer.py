
import heapq

def return_n_smallest_chars(s):

    smallest_chars = heapq.nsmallest(70, s)

    smallest_chars.sort(reverse=True)

    return smallest_chars
