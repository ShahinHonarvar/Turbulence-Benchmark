def palindromes_between_indices(str1):
    str1 = str(str1)
    s = set()
    for i in range(len(str1) - 2):
        c = str1[i:i + 2]
        if c[::-1] in s:
            s.add(c)
    return s
