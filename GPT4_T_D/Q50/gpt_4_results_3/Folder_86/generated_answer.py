
def if_contains_anagrams(lst):
    from collections import Counter
    def are_anagrams(s1, s2):
        return Counter(s1) == Counter(s2)
    anagrams = set()
    for i in range(len(lst)):
        if len(lst[i]) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if len(lst[j]) < 3:
                continue
            if are_anagrams(lst[i].lower(), lst[j].lower()):
                anagrams.add((lst[i], lst[j]))
    if len(anagrams) >= 115:
        return True
    else:
        return False
