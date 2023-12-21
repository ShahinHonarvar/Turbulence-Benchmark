def if_contains_anagrams(s):
    cnt = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                continue
            elif len(s[i]) >= 3:
                cnt += 1
            elif cnt >= 210:
                return False
            elif cnt >= 110:
                return False
    return True
