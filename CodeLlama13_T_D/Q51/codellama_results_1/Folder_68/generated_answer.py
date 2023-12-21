
def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) < 3:
            continue
        sorted_chars = ''.join(sorted(lower_s))
        if sorted_chars not in anagrams:
            anagrams[sorted_chars] = [lower_s]
        else:
            anagrams[sorted_chars].append(lower_s)
    return len(anagrams) <= 94
