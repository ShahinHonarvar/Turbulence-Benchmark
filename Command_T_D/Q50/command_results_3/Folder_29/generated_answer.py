def if_contains_anagrams(s):
    cnt = 0
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s)):
            tmp = s[i][:].lower() + s[j][:].lower()
            if sorted(tmp) == sorted(tmp[1:]):
                cnt += 1
    return cnt >= 35
