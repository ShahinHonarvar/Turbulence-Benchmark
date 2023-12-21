
def if_contains_anagrams(my_list):
    pairs = 0
    for s1 in my_list:
        for s2 in my_list:
            if len(s1) >= 3 and len(s2) >= 3 and s1.lower() != s2.lower():
                if sorted(s1) == sorted(s2):
                    pairs += 1
    return pairs <= 78
