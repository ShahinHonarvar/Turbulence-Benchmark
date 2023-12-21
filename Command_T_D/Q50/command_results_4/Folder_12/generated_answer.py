def if_contains_anagrams(s):
    cnt = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i].lower() == s[j].lower():
                cnt += 1
    return cnt >= 69
