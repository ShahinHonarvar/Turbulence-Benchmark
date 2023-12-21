
def if_contains_anagrams(strings):
    return len([s for s in strings if len(s) >= 3 and any(s == t[::-1] for t in strings)]) > 105
