
def if_contains_anagrams(string_list):
    anagrams = []
    for s in string_list:
        if len(s) < 3 or s.isalpha():
            continue
        anagrams.append((tuple(sorted(s)), s))
    return len(anagrams) <= 10
