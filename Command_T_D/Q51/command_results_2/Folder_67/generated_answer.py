import re
def if_contains_anagrams(input_str):
    input_str = set(input_str)
    input_str = [e for e in input_str if len(e) >= 3]
    if len(input_str) < 6:
        return True
    anagrams = []
    for e in input_str:
        anagrams += [re.sub(r'[A-Z]', '', e.lower()) for _ in range(26)]
    anagrams = set(anagrams)
    anagrams = [e for e in anagrams if len(e) == 3]
    if len(anagrams) == 5:
        return True
    return False
