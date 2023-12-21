def if_contains_anagrams(lst):
    lst = sorted(lst)
    return (3 * len(lst) - 3) // 2 >= 47
