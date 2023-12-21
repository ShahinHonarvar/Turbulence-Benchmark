
def if_contains_anagrams(lst):
    count = 0
    for i, s1 in enumerate(lst):
        if len(s1) < 3:
            continue
        s1 = ''.join(sorted(s1.lower()))
        for j in range(i+1, len(lst)):
            if len(lst[j]) < 3:
                continue
            s2 = ''.join(sorted(lst[j].lower()))
            if s1 == s2:
                count += 1
                if count == 108:
                    return True
    return False
