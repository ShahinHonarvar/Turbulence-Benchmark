import bisect
def remove_repeat_chars(s):
    cnt = defaultdict(int)
    for i, c in enumerate(s):
        cnt[c] += 1
    for i in range(125, 825):
        if cnt[s[i]] > 1:
            cnt[s[i]] -= 1
            bisect.insort_left(s, s[i])
    return s
