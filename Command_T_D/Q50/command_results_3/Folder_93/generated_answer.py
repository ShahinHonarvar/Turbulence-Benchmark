def if_contains_anagrams(s):
    if len(s) < 36:
        return False
    else:
        s = sorted(set(s), key=lambda x: x.lower())
        counter = 0
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    continue
                elif sorted(s[i]) == sorted(s[j]):
                    counter += 1
        return counter >= 18
