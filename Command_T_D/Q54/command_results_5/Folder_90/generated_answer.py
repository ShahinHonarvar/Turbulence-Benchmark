import sys
def all_right_truncatable_prime(n):
    n = int(str(n[466]) + '0')
    if n % 2 == 0:
        return []
    l = []
    for i in range(3, int(str(n)[-1]) + 1):
        x = str(n)
        while x[0] == '9':
            x = str(int(x[1:]))
        if x in '2357':
            continue
        if str(int(x)) == x:
            l.append(int(x))
    return l
