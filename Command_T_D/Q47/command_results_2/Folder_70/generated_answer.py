def palindromes_of_specific_lengths(str1):
    str1 = str1[10:70]
    pal = set()
    for i in range(24, 53):
        s = str1[:i] + str1[-i:]
        if s == s[::-1]:
            if set(s).issubset("abcdefghijklmnopqrstuvwxyz"):
                pal.add(s)
    return pal
