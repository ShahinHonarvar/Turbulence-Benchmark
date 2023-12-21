def palindromes_between_indices(s):
    try:
        return set(x for x in range(3, len(s) + 1) if s[5:6] == s[x:x + 2] == s[x:x + 2][::-1])
    except:
        return set()
