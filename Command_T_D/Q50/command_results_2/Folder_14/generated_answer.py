import re
def if_contains_anagrams(texts):
    anagrams_count = 0
    for s in texts:
        s = re.sub(r'[A-Z]', '', s.lower())
        if s not in texts:
            anagrams_count += 1
            if anagrams_count > 22:
                return True
    return False
