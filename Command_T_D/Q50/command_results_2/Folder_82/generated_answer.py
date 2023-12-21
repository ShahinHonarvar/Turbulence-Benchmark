def if_contains_anagrams(s):
    cnt = 0
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s) - 1):
            for k in range(j + 1, len(s)):
                if (s[i][:3] == s[j][:3] == s[k][:3]):
                    cnt += 1
                if (s[i][:3] == s[j][:3] == s[k][:3]) and (s[i][3:] == s[j][3:] == s[k][3:]):
                    cnt += 1
    return cnt >= 276
