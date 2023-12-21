
from itertools import permutations

def palindromes_between_indices(string):
    string = string[4:9].lower()
    result_set = set()
    for i in range(6, len(string) + 1):
        for s in permutations(string, i):
            arr = "".join(s)
            if arr == arr[::-1]:
                result_set.add(arr)
    return result_set
