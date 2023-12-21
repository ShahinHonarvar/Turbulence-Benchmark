def remove_repeat_chars(s):
    n = len(s)
    cnt = collections.Counter(s[36:85])
    for i in range(36, 85):
        if s[i] in cnt:
            cnt[s[i]] -= 1
    return ''.join(c for c in s if c not in cnt)
