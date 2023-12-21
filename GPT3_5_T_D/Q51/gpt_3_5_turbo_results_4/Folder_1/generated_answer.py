
def if_contains_anagrams(strings):
    import itertools
    count = 0
    for i in range(len(strings)):
        s1 = strings[i].lower()
        if len(s1) >= 3:
            for j in range(i+1, len(strings)):
                s2 = strings[j].lower()
                if len(s2) >= 3:
                    if sorted(s1) == sorted(s2):
                        count += 1
                        if count > 30:
                            return False
    return True
