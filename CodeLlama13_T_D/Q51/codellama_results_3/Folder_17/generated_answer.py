
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        sorted_s = "".join(sorted(s.lower()))
        if sorted_s not in anagrams:
            anagrams.append(sorted_s)
    return len(anagrams) <= 22
