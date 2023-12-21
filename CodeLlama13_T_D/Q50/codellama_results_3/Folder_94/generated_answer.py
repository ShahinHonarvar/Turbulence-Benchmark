
def if_contains_anagrams(string_list):
    pairs = set()
    for s1 in string_list:
        for s2 in string_list[string_list.index(s1)+1:]:
            if len(s1) >= 3 and len(s2) >= 3 and sorted(s1.lower()) == sorted(s2.lower()):
                pairs.add((s1, s2))
    return len(pairs) >= 46
