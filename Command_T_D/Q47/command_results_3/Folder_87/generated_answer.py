def palindromes_of_specific_lengths(s):
    for i in range(11, 94):
        if i >= 33 and i <= 53:
            for j in range(i, i + 34):
                if s[j] == s[j][::-1]:
                    yield s[j:j + 34]
