def if_contains_anagrams(s):
    if len(s) < 55:
        return True
    s.sort()
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            continue
        elif len(s[i]) < 3:
            continue
        elif s[i].lower() == s[i + 1].lower():
            return False
    return True
