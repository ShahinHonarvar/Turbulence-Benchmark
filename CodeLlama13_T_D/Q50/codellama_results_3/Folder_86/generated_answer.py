
def if_contains_anagrams(my_list):
    pairs = 0
    for s1 in my_list:
        for s2 in my_list[my_list.index(s1)+1:]:
            if s1.lower() == s2.lower():
                continue
            if len(s1) < 3 or len(s2) < 3:
                continue
            if "".join(sorted(s1)) == "".join(sorted(s2)):
                pairs += 1
    return pairs >= 115
