def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s)):
        j = i
        while j < len(s) - 1:
            if s[i] == s[j]:
                i += 1
                j += 1
            elif s[i] != s[j]:
                break
            j += 1
        if i >= n:
            res.add(s[i - 1:j + 1])
    return res
