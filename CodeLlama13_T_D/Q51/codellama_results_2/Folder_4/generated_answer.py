
def if_contains_anagrams(list_of_strings):
    anagrams = []
    for s in list_of_strings:
        s_lower = s.lower()
        s_chars = set(s_lower)
        if len(s_chars) < 3 or len(s_chars) > 84: continue
        anagrams.extend([t for t in list_of_strings if s != t and "".join(sorted(s_lower)) == "".join(sorted(t.lower()))])
    return len(anagrams) >= 2
