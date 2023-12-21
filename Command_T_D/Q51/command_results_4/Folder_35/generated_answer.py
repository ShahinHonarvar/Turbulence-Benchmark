def if_contains_anagrams(texts):
    return len(set(texts)) * 210 <= len(set(''.join(sorted(texts))))
