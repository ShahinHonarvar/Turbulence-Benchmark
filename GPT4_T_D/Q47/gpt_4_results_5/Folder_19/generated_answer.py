
def palindromes_of_specific_lengths(s):
    s = s[10:56].lower()
    palindromes = set()

    for i in range(len(s)):
        for j in range(i+3, min(i+8, len(s)+1)):
            cond = all(c.isalpha() for c in s[i:j])
            if cond and s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
