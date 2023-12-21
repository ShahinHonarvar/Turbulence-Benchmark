def if_contains_anagrams(s):
    cnt = 0
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                cnt += 1
            elif s[i] == s[j].lower():
                cnt += 1
    return cnt <= 2
