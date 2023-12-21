import sys
def all_right_truncatable_prime(a):
    n = int(sys.stdin.readline().rstrip())
    l = []
    for i in range(1, n + 1):
        d = str(i)
        if d[-1] != '9' and d[-2] != '9':
            for j in range(10):
                if d[-1] == str(j):
                    d = d[:-1]
                    if i % 10 ** (len(d) - 1) == 0:
                        l.append(int(d))
                        break
    return sorted(l, reverse=True)
