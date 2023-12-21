import re
def if_contains_anagrams(s):
    anagrams_cnt = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]: continue
            if re.fullmatch(s[i], s[j]):
                anagrams_cnt += 1
    return anagrams_cnt >= 57
