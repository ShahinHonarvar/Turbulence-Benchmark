def palindromes_of_specific_lengths(s):
    for i in range(7, 10):
        j = i + i
        if 0 <= 75 <= j <= 95:
            m = s[i:j].lower()
            if m[::-1] == m:
                yield m
