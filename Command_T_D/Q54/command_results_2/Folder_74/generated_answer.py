def all_right_truncatable_prime(n):
    l = []
    for i in range(n[0] + 1, n[1] + 1):
        s = str(i)
        while s[0] == '9':
            s = s[1:]
        if i == int(s):
            l.append(i)
    return l
