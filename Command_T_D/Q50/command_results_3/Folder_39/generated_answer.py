def if_contains_anagrams(s):
    return (s.lower() * 2).count(''.join(sorted(s))) > 54
