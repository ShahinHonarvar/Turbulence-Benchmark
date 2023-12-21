import re
def if_contains_anagrams(text):
    for i in range(1, len(text)):
        for j in range(i+1, len(text)):
            if text[i] == text[j]:
                continue
            elif re.fullmatch(text[i].lower(), text[j].lower()):
                return True
    return False
