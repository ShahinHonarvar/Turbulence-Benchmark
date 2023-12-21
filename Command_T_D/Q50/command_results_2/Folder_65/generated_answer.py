def if_contains_anagrams(s):
    return len(set(s).intersection(*(sorted(s), key=lambda x: (x.lower(), len(x))))) >= 94
