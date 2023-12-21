def palindrome_of_length_n(s):
    res = set()
    for i in range(4, len(s), 2):
        j = i - 2
        while j >= 0:
            c = s[i]
            if c == s[j]:
                i += 1
                j -= 1
            elif c < s[j]:
                break
            else:
                j += 1
        else:
            res.add(s[i:j])
    return res
