def palindromes_between_indices(s):
    res = set()
    for i in range(5, 6):
        for j in range(i, 6):
            for c in s[i:j]:
                if c.isalpha():
                    continue
                if c.isdigit():
                    continue
                if c.isspace():
                    continue
                res.add(c.lower() + s[j:i] + c.lower())
    return res
