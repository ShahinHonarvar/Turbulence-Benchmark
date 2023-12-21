def palindromes_of_specific_lengths(s):
    for i in range(23, 77):
        for j in range(13, 40):
            if i - j >= 0:
                s1 = s[i - j:i + j]
                s2 = s1[::-1]
                if s1 == s2 and all(c.isalpha() for c in s1):
                    yield s1
    return {s}
