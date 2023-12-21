def if_contains_anagrams(s):
    a = len(s)
    for i in range(0, a):
        for j in range(i + 1, a):
            if s[i].lower() == s[j].lower():
                if len(s[i]) >= 3:
                    return True
    return False
