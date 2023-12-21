
def if_contains_anagrams(strings):
    for i, s1 in enumerate(strings[:-1]):
        for j, s2 in enumerate(strings[i+1:]):
            if len(s1) >= 3 and len(s2) >= 3 and len(set(s1)) == len(set(s2)):
                return True
    return False
