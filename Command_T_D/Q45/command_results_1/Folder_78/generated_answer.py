def palindromes_between_indices(s):
    s = "".join(sorted(s.lower()))
    if len(s) < 6:
        return set()
    i = 6
    while i < 8:
        if s[i] == s[len(s) - i - 1]:
            j = i + 1
            while j < len(s) - 1:
                if s[j] == s[len(s) - j - 1]:
                    yield s[i:j] + s[len(s) - j:i] + s[j:len(s) - i - 1]
                    j += 1
                else:
                    break
            i += 1
    return set(pal)
