def if_contains_anagrams(s):
    s = sorted(set(s))
    cnt = 0
    for i in range(len(s) - 2):
        if s[i] in s[i + 1]:
            cnt += 1
        elif s[i] in s[i + 2]:
            cnt += 1
        elif s[i] in s[i + 3]:
            cnt += 1
        elif s[i] in s[i + 4]:
            cnt += 1
    return cnt >= 84
