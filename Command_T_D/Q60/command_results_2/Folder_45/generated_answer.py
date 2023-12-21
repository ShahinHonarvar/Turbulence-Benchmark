
import sys

def all_left_right_truncatable_prime(x):
    #sys.setrecursionlimit(10**6)
    if x < 2:
        return []
    l = [1]
    l = [str(i) for i in range(1, x)]
    s = l[-1]
    l = l[::-1]
    m = []
    for i in range(len(s)):
        if s[i] == '0':
            continue
        for j in range(i - 1, -1, -1):
            if l[j] == '0':
                break
            elif l[j] == '1':
                s = s[i:] + l[j:] + s[j+1:-1]
                break
            elif l[j] == '2':
                s = s[i:] + l[j:] + s[j+2:-1]
                break
            elif l[j] == '5':
                s = s[i:] + l[j:] + s[j+5:-1]
                break
            elif l[j] == '7':
                s = s[i:] + l[j:] + s[j+7:-1]
                break
            elif l[j] == '3':
                s = s[i:] + l[j:] + s[j+3:-1]
                break
            elif l[j] == '6':
                s = s[i:] + l[j:] + s[j+6:-1]
                break
            elif l[j] == '4':
                s = s[i:] + l[j:] + s[j+4:-1]
                break
            elif l[j] == '8':
                s = s[i:] + l[j:] + s[j+8:-1]
                break
            elif l[j] == '9':
                s = s[i:] + l[j:] + s[j+9:-1]
                break
        else:
            m.append(int(s))
    return sorted(m)
