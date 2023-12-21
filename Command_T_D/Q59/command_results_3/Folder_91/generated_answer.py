def all_left_truncatable_prime(n):
    res = []
    for i in range(3, n[0] + 1):
        s = str(i)
        cnt = 0
        for j in range(len(s)):
            if s[j] == '0':
                break
            cnt += 1
        if cnt == len(s):
            res += [int(s)]
    return res
