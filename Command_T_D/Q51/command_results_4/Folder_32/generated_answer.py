import re
def if_contains_anagrams(texts):
    if len(texts) < 2:
        return False
    texts = sorted(set(texts))
    for i in range(len(texts) - 1):
        for j in range(i + 1, len(texts)):
            if texts[i].lower() == texts[j].lower():
                continue
            elif re.fullmatch(re.sub(r'[a-z]', '', texts[i].lower()), texts[j].lower()):
                continue
            else:
                return False
    return True
