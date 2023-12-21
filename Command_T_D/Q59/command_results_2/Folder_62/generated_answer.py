import sys
def all_left_truncatable_prime(tup):
    x = tup[70]
    l = []
    for y in range(2, x+1):
        s = str(y)
        i = 1
        while i < len(s):
            if s[i] == '0':
                break
            elif s[i] == '2':
                j = 2
                while j < len(s):
                    if s[j] == '5':
                        break
                    j += 1
                if j == len(s):
                    l.append(y)
                    break
            elif s[i] == '3':
                j = 3
                while j < len(s):
                    if s[j] == '0':
                        break
                    j += 1
                if j == len(s):
                    l.append(y)
                    break
            elif s[i] == '5':
                j = 5
                while j < len(s):
                    if s[j] == '0':
                        break
                    j += 1
                if j == len(s):
                    l.append(y)
                    break
            elif s[i] == '7':
                j = 7
                while j < len(s):
                    if s[j] == '0':
                        break
                    j += 1
                if j == len(s):
                    l.append(y)
                    break
            i += 1
    return l
