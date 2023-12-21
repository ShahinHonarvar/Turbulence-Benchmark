
def if_contains_anagrams(strings):
    for i in range(len(strings)):
        s1 = strings[i].lower()
        for j in range(i+1, len(strings)):
            s2 = strings[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1) == sorted(s2):
                    return True
    return False
