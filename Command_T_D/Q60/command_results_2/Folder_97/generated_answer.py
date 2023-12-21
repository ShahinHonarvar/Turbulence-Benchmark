
def all_left_right_truncatable_prime(n):
    s = str(n)
    i = j = 0
    while j < len(s):
        if s[i] == s[j]:
            i += 1
            j += 1
        elif s[i] > s[j]:
            j += 1
        else:
            break
    return sorted(list(range(3, int(s[:i]) + 1, 2)), key=lambda x: str(x))
