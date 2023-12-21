def if_contains_anagrams(s):
    s = sorted(s)
    cnt = 0
    for i in range(len(s)):
        if i == 0:
            continue
        elif s[i] == s[i - 1]:
            continue
        elif s[i][: len(s[i - 1])] == s[i - 1]:
            cnt += 1
        elif s[i][: len(s[i - 1])] == s[i - 1][::-1]:
            cnt += 1
    return cnt >= 74
