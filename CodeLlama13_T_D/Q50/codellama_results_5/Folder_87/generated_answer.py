
def if_contains_anagrams(strings):
    return len([s for s in strings if len(s) >= 3 and (len(set(s)) == 1 or len([ss for ss in strings if sorted(ss) == sorted(s)])) >= 88]) > 0
