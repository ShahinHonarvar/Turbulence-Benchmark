def if_contains_anagrams(s):
    if len(s) >= 84:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    continue
                elif len(s[i]) >= 3 and len(s[j]) >= 3:
                    if sorted(s[i]) == sorted(s[j]):
                        return True
        return False
    else:
        return False
