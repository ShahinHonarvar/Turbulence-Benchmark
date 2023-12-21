import re
def if_contains_anagrams(input_list):
    anagrams = set()
    for s in input_list:
        if len(s) >= 3:
            lower = s.lower()
            if lower in anagrams:
                return True
            if re.sub(r'[^a-z]', '', lower) in anagrams:
                return True
            anagrams.add(lower)
            if len(anagrams) > 69:
                return False
    return True
