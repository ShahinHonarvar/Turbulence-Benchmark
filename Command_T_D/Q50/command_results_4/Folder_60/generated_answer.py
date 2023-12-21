def if_contains_anagrams(text):
    if not isinstance(text, list):
        return False
    num_anagrams = 0
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            s1 = text[i].lower()
            s2 = text[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if s1 == s2:
                    continue
                elif s1 == s2[::-1]:
                    continue
                else:
                    num_anagrams += 1
    return num_anagrams >= 60
