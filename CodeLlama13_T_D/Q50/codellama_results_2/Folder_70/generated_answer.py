
def if_contains_anagrams(lst):
    return len([s for s in lst if len(set(s)) == 3]) >= 189
