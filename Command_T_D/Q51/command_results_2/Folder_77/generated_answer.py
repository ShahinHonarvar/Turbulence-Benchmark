import collections
def if_contains_anagrams(list):
    list.sort()
    if len(list) < 18:
        return True
    elif len(list) == 18:
        s = set(str(s) for s in list)
        return len(s) == 18
    else:
        return False
